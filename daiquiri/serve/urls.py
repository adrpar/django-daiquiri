from django.conf.urls import url, include

from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'rows', RowViewSet, base_name='row')
router.register(r'columns', ColumnViewSet, base_name='column')

urlpatterns = [
    url(r'^table/(?P<database_name>[A-Za-z0-9_]+)/(?P<table_name>[A-Za-z0-9_]+)/$', serve_table, name='serve_table'),

    # rest api
    url(r'^api/', include(router.urls, namespace='serve')),
]
