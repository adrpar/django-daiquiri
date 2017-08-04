from django.contrib import admin

from .models import QueryJob, Example


class QueryJobAdmin(admin.ModelAdmin):
    search_fields = ('id', 'owner__username', 'phase')
    list_display = ('id', 'owner', 'phase', 'creation_time', 'database_name', 'table_name', 'nrows')


class ExampleAdmin(admin.ModelAdmin):
    search_fields = ('name', 'query_string')
    list_display = ('order', 'name', 'query_string')
    list_display_links = ('name', )


admin.site.register(QueryJob, QueryJobAdmin)
admin.site.register(Example, ExampleAdmin)
