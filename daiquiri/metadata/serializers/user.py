from rest_framework import serializers

from ..models import Database, Table, Column, Function


class ColumnSerializer(serializers.ModelSerializer):

    class Meta:
        model = Column
        fields = (
            'id',
            'order',
            'name',
            'query_string',
            'description',
            'unit',
            'ucd',
            'utype',
            'datatype',
            'size',
            'principal',
            'indexed',
            'std'
        )


class TableSerializer(serializers.ModelSerializer):

    columns = serializers.SerializerMethodField()

    class Meta:
        model = Table
        fields = (
            'id',
            'order',
            'name',
            'query_string',
            'description',
            'type',
            'utype',
            'columns'
        )

    def get_columns(self, obj):
        # filter the columns which are published for the groups of the user
        queryset = obj.columns.filter(groups__in=self.context['request'].user.groups.all())
        return ColumnSerializer(queryset, context=self.context, many=True).data


class DatabaseSerializer(serializers.ModelSerializer):

    tables = serializers.SerializerMethodField()

    class Meta:
        model = Database
        fields = (
            'id',
            'order',
            'name',
            'query_string',
            'description',
            'utype',
            'tables'
        )

    def get_tables(self, obj):
        # filter the tables which are published for the groups of the user
        queryset = obj.tables.filter(groups__in=self.context['request'].user.groups.all())
        return TableSerializer(queryset, context=self.context, many=True).data


class FunctionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Function
        fields = (
            'id',
            'order',
            'name',
            'query_string'
        )
