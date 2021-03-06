app.factory('QueryService', ['$resource', '$injector', '$q', '$filter', 'PollingService', 'DownloadService', 'TableService', 'BrowserService', function($resource, $injector, $q, $filter, PollingService, DownloadService, TableService, BrowserService) {

    /* get the base url */

    var baseurl = angular.element('meta[name="baseurl"]').attr('content');

    /* configure resources */

    var resources = {
        status: $resource(baseurl + 'query/api/status/'),
        forms: $resource(baseurl + 'query/api/forms/'),
        dropdowns: $resource(baseurl + 'query/api/dropdowns/'),
        jobs: $resource(baseurl + 'query/api/jobs/:id/:detail_route/'),
        examples: $resource(baseurl + 'query/api/examples/user/'),
        queues: $resource(baseurl + 'query/api/queues/'),
        querylanguages: $resource(baseurl + 'query/api/querylanguages/'),
        databases: $resource(baseurl + 'metadata/api/databases/user/'),
        functions: $resource(baseurl + 'metadata/api/functions/user/'),
    };

    /* initialise the browser service */

    BrowserService.init('databases', ['databases', 'tables', 'columns'])
    BrowserService.init('columns', ['columns'], true)
    BrowserService.init('functions', ['functions'])
    BrowserService.init('examples', ['examples'])

    /* create the query service */

    var service = {
        forms: {},
        dropdowns: {},
        values: {},
        errors: {}
    };

    service.init = function() {
        // fetch queues,  query languages and then load forms
        service.queues = resources.queues.query();
        service.query_languages = resources.querylanguages.query();

        $q.all([service.queues.$promise, service.query_languages.$promise]).then(function(){
            service.active_queue = service.queues[0].id;

            resources.forms.query(function(response) {
                angular.forEach(response, function(form) {
                    service.forms[form.key] = $injector.get(form.form_service);
                });

                // activate first form
                service.forms[response[0].key].activate();
            });
        });

        // load dropdowns
        resources.dropdowns.query(function(response) {
            angular.forEach(response, function(dropdown) {
                service.dropdowns[dropdown.key] = $injector.get(dropdown.dropdown_service);
                service.dropdowns[dropdown.key].options = dropdown.options;
            });
        });

        // fetch status
        service.fetchStatus();

        // fetch functions
        resources.functions.query(function(response) {
            BrowserService.render('functions', response);
        });

        // fetch examples
        resources.examples.query(function(response) {
            BrowserService.render('examples', response);
        });

        // fetch databases
        resources.databases.query(function(response) {
            service.databases = response;

            service.columns = []
            angular.forEach(service.databases, function(database) {
                angular.forEach(database.tables, function(table) {
                    angular.forEach(table.columns, function(column) {
                        var column_copy = angular.copy(column);
                        column_copy.name = database.name + '.' + table.name + '.' + column.name;
                        service.columns.push(column_copy);
                    });
                });
            });

            // load user database when databases have been fetched
            service.fetchUserDatabase();
        });

        // fetch joblist
        service.fetchJobs();

        // activate overview tab
        service.tab = 'overview';

        // start the polling service
        PollingService.init();
        PollingService.register('status', service.fetchStatus);
        PollingService.register('jobs', service.fetchJobs);
        PollingService.register('database', service.fetchUserDatabase);

        // load the download service
        service.downloads = DownloadService;
    };

    service.fetchStatus = function() {
        resources.status.query(function(response) {
            service.status = response[0];
        }).$promise;
    };

    service.fetchUserDatabase = function() {
        return resources.jobs.query({
            'detail_route': 'tables'
        }, function(response) {
            var user_database = response[0];

            var user_columns = [];
            angular.forEach(user_database.tables, function(table) {
                angular.forEach(table.columns, function(column) {
                    var column_copy = angular.copy(column);
                    column_copy.name = user_database.name + '.' + table.name + '.' + column.name;
                    user_columns.push(column_copy);
                });
            });

            BrowserService.render('databases', service.databases.concat(user_database));
            BrowserService.render('columns', service.columns.concat(user_columns));
        }).$promise;
    }

    service.fetchJobs = function() {
        return resources.jobs.query(function(response) {
            service.jobs = response;

            if (service.job) {
                // get the phase of the current job in the jobs list
                var phase = $filter('filter')(service.jobs, {'id': service.job.id})[0].phase;

                // if the phase has changed, fetch it again
                if (phase != service.job.phase) {
                    service.fetchJob(service.job);
                }
            }

        }).$promise;
    };

    service.fetchJob = function(job) {
        return resources.jobs.get({id: job.id}, function(response) {
            service.job = response;
            service.job.time_queue = moment.duration(moment(service.job.start_time) - moment(service.job.creation_time)).seconds();
            service.job.time_query = moment.duration(moment(service.job.end_time) - moment(service.job.start_time)).seconds();

            // get the phase of the current job in the jobs list
            var phase = $filter('filter')(service.jobs, {'id': service.job.id})[0].phase;

            // if the phase has changed, fetch the job list again
            if (phase != service.job.phase) {
                service.fetchJobs();
            }

        }).$promise;
    };

    service.activateForm = function(key) {
        service.form = key;
        service.job = null;
    };

    service.activateJob = function(job) {
        service.form = null;
        service.fetchJob(job).then(function() {

            if (service.job.phase == 'COMPLETED') {
                TableService.init(service.job.database_name, service.job.table_name);
            }

            CodeMirror.runMode(service.job.query, "text/x-mariadb", angular.element('#query')[0]);
            CodeMirror.runMode(service.job.actual_query, "text/x-mariadb", angular.element('#actual-query')[0]);
        });
    };

    service.submitJob = function(values) {
        values = angular.extend({}, values, {
            'queue': service.active_queue
        });

        return resources.jobs.save(values).$promise.then(function(job) {
            service.fetchStatus();
            service.fetchJobs();
            service.activateJob(job);
        });
    };

    service.showModal = function(modal, job) {
        service.errors = {};

        if (angular.isDefined(job)) {
            service.values = job;
        }

        $('#' + modal + '-modal').modal('show');
    };

    service.renameJob = function() {
        resources.jobs.update({id: service.values.id}, service.values).$promise.then(function() {
            service.fetchJobs();
            $('.modal').modal('hide');
        }, function(response) {
            service.errors = response.data;
        });
    };

    service.killJob = function() {
        resources.jobs.update({id: service.values.id, detail_route: 'kill'}, {}, function() {
            service.fetchStatus();
            service.fetchJobs();
            $('.modal').modal('hide');
        });
    };

    service.removeJob = function() {
        var index = service.jobs.indexOf($filter('filter')(service.jobs, {'id': service.job.id})[0]);

        var next_job;
        if (index == 0) {
            next_job = service.jobs[1];
        } else {
            next_job = service.jobs[index - 1];
        }

        resources.jobs.delete({id: service.values.id}, function() {
            service.fetchStatus();
            service.fetchJobs();
            service.activateJob(next_job);
            $('.modal').modal('hide');
        });
    };

    return service;

}]);
