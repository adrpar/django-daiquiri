from django.db import models, ProgrammingError
from django.contrib.auth.models import Group
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from daiquiri.core.adapter import get_adapter

from .managers import (
    DatabasePermissionsManager,
    TablePermissionsManager,
    ColumnPermissionsManager,
    FunctionPermissionsManager
)

LICENSE_CC0 = 'CC0'
LICENSE_PD = 'PD'
LICENSE_BY = 'BY'
LICENSE_BY_SA = 'BY_SA'
LICENSE_BY_ND = 'BY_ND'
LICENSE_BY_NC = 'BY_NC'
LICENSE_BY_NC_SA = 'BY_NC_SA'
LICENSE_BY_NC_ND = 'BY_NC_ND'
LICENSE_CHOICES = (
    (LICENSE_CC0, 'CC0 1.0 Universal (CC0 1.0)'),
    (LICENSE_PD, 'Public Domain Mark'),
    (LICENSE_BY, 'Attribution 4.0 International (CC BY 4.0)'),
    (LICENSE_BY_SA, 'Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)'),
    (LICENSE_BY_ND, 'Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)'),
    (LICENSE_BY_NC, 'Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)'),
    (LICENSE_BY_NC_SA, 'Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)'),
    (LICENSE_BY_NC_ND, 'Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)')
)

LICENSE_URLS = {
    LICENSE_CC0: 'https://creativecommons.org/publicdomain/zero/1.0/',
    LICENSE_PD: None,
    LICENSE_BY: 'https://creativecommons.org/licenses/by/4.0/',
    LICENSE_BY_SA: 'https://creativecommons.org/licenses/by-sa/4.0/',
    LICENSE_BY_ND: 'https://creativecommons.org/licenses/by-nd/4.0/',
    LICENSE_BY_NC: 'https://creativecommons.org/licenses/by-nc/4.0/',
    LICENSE_BY_NC_SA: 'https://creativecommons.org/licenses/by-nc-sa/4.0/',
    LICENSE_BY_NC_ND: 'https://creativecommons.org/licenses/by-nc-nd/4.0/'
}


@python_2_unicode_compatible
class Database(models.Model):

    objects = models.Manager()
    permissions = DatabasePermissionsManager()

    order = models.IntegerField(null=True, blank=True)

    name = models.CharField(max_length=256)

    title = models.CharField(max_length=256, null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)

    attribution = models.TextField(null=True, blank=True)

    license = models.CharField(max_length=8, choices=LICENSE_CHOICES, null=True, blank=True)
    pid = models.URLField(max_length=256, null=True, blank=True)

    utype = models.CharField(max_length=256, null=True, blank=True)

    groups = models.ManyToManyField(Group, blank=True)

    class Meta:
        ordering = ('order', )

        verbose_name = _('Database')
        verbose_name_plural = _('Databases')

        permissions = (('view_database', 'Can view Database'),)

    def __str__(self):
        return self.name

    @property
    def query_string(self):
        return get_adapter('data').escape_identifier(self.name)

    @property
    def license_label(self):
        return dict(LICENSE_CHOICES)[self.license]

    @property
    def license_url(self):
        return LICENSE_URLS[self.license]


@python_2_unicode_compatible
class Table(models.Model):

    TYPE_TABLE = 'table'
    TYPE_VIEW = 'view'
    TYPE_CHOICES = (
        (TYPE_TABLE, _('Table')),
        (TYPE_VIEW, _('View'))
    )

    objects = models.Manager()
    permissions = TablePermissionsManager()

    database = models.ForeignKey(Database, related_name='tables')

    order = models.IntegerField(null=True, blank=True)

    name = models.CharField(max_length=256)

    title = models.CharField(max_length=256, null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)

    attribution = models.TextField(null=True, blank=True)

    license = models.CharField(max_length=8, choices=LICENSE_CHOICES, null=True, blank=True)
    pid = models.URLField(max_length=256, null=True, blank=True)

    type = models.CharField(max_length=8, choices=TYPE_CHOICES)
    utype = models.CharField(max_length=256, null=True, blank=True)

    groups = models.ManyToManyField(Group, blank=True)

    class Meta:
        ordering = ('database__order', 'order', )

        verbose_name = _('Table')
        verbose_name_plural = _('Tables')

        permissions = (('view_table', 'Can view Table'),)

    def __str__(self):
        return self.database.name + '.' + self.name

    def save(self, *args, **kwargs):
        super(Table, self).save(*args, **kwargs)

        try:
            get_adapter('metadata').store_table_metadata(self.database.name, self.name, {
                'order': self.order,
                'name': self.name,
                'description': self.description,
                'type': self.type,
                'utype': self.utype
            })
        except ProgrammingError:
            pass

    @property
    def query_string(self):
        adapter = get_adapter('data')
        return '%(database)s.%(table)s' % {
            'database': adapter.escape_identifier(self.database.name),
            'table': adapter.escape_identifier(self.name)
        }

    @property
    def license_label(self):
        return dict(LICENSE_CHOICES)[self.license]

    @property
    def license_url(self):
        return LICENSE_URLS[self.license]


@python_2_unicode_compatible
class Column(models.Model):

    objects = models.Manager()
    permissions = ColumnPermissionsManager()

    table = models.ForeignKey(Table, related_name='columns')

    order = models.IntegerField(null=True, blank=True)

    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)

    unit = models.CharField(max_length=256, null=True, blank=True)
    ucd = models.CharField(max_length=256, null=True, blank=True)
    utype = models.CharField(max_length=256, null=True, blank=True)

    datatype = models.CharField(max_length=256, null=True, blank=True)
    size = models.IntegerField(null=True, blank=True, help_text=_('The length of variable length datatypes, e.g. varchar(256).'))

    principal = models.BooleanField(default=False, help_text=_('This column is considered a core part of the content.'))
    indexed = models.BooleanField(default=False, help_text=_('This column is indexed.'))
    std = models.BooleanField(default=False, help_text=_('This column is defined by some standard.'))

    groups = models.ManyToManyField(Group, blank=True)

    class Meta:
        ordering = ('table__database__order', 'table__order', 'order', )

        verbose_name = _('Column')
        verbose_name_plural = _('Columns')

        permissions = (('view_column', 'Can view Column'),)

    def __str__(self):
        return self.table.database.name + '.' + self.table.name + '.' + self.name

    def save(self, *args, **kwargs):
        super(Column, self).save(*args, **kwargs)

        try:
            get_adapter('metadata').store_column_metadata(self.table.database.name, self.table.name, self.name, {
                'order': self.order,
                'name': self.name,
                'description': self.description,
                'unit': self.unit,
                'ucd': self.ucd,
                'utype': self.utype,
                'datatype': self.datatype,
                'size': self.size,
                'principal': self.principal,
                'indexed': self.indexed,
                'std': self.std
            })
        except ProgrammingError:
            pass

    @property
    def query_string(self):
        return get_adapter('data').escape_identifier(self.name)


@python_2_unicode_compatible
class Function(models.Model):

    objects = models.Manager()
    permissions = FunctionPermissionsManager()

    order = models.IntegerField(null=True, blank=True)

    name = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)

    query_string = models.CharField(max_length=256)

    groups = models.ManyToManyField(Group, blank=True)

    class Meta:
        ordering = ('order', )

        verbose_name = _('Function')
        verbose_name_plural = _('Functions')

        permissions = (('view_function', 'Can view Function'),)

    def __str__(self):
        return self.name
