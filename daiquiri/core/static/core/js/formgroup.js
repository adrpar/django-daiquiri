angular.module('core')

.directive('formgroup', function() {

    return {
        scope: {
            id: '@',
            label: '@',
            help: '@',
            model: '=',
            errors: '=',
            mode: '@',
            options: '=',
            optionsLabel: '@',
            optionsFilter: '=',
            optionsNull: '@'
        },
        templateUrl: function(element, attrs) {
            var staticurl = angular.element('meta[name="staticurl"]').attr('content');
            return staticurl + 'core/html/formgroup_' + attrs.type + '.html';
        }
    };
});
