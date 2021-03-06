from rest_framework.routers import Route, SimpleRouter


class UWSRouter(SimpleRouter):
    routes = [
        Route(
            url=r'^{prefix}$',
            mapping={'get': 'list', 'post': 'create'},
            name='{basename}-list',
            initkwargs={'suffix': 'List'}
        ),
        Route(
            url=r'^{prefix}/{lookup}$',
            mapping={'get': 'retrieve', 'post': 'update', 'delete': 'destroy'},
            name='{basename}-detail',
            initkwargs={'suffix': 'Detail'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/results$',
            mapping={'get': 'get_results'},
            name='{basename}-results',
            initkwargs={'suffix': 'Results'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/parameters$',
            mapping={'get': 'get_parameters'},
            name='{basename}-parameters',
            initkwargs={'suffix': 'Parameters'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/destruction$',
            mapping={'get': 'get_destruction', 'post': 'post_destruction'},
            name='{basename}-destruction',
            initkwargs={'suffix': 'Destruction'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/executionduration$',
            mapping={'get': 'get_executionduration', 'post': 'post_executionduration'},
            name='{basename}-executionduration',
            initkwargs={'suffix': 'Executionduration'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/phase$',
            mapping={'get': 'get_phase', 'post': 'post_phase'},
            name='{basename}-phase',
            initkwargs={'suffix': 'Phase'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/error$',
            mapping={'get': 'get_error'},
            name='{basename}-error',
            initkwargs={'suffix': 'Error'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/quote$',
            mapping={'get': 'get_quote'},
            name='{basename}-quote',
            initkwargs={'suffix': 'Quote'}
        ),
        Route(
            url=r'^{prefix}/{lookup}/owner$',
            mapping={'get': 'get_owner'},
            name='{basename}-owner',
            initkwargs={'suffix': 'Owner'}
        ),
    ]
