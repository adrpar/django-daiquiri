from django.conf.urls import url, include

from daiquiri.uws.routers import UWSRouter

from .viewsets import QueryJobsViewSet

router = UWSRouter(trailing_slash=False)
router.register(r'query', QueryJobsViewSet, base_name='query')

urlpatterns = [
    url(r'', include(router.urls)),
]
