from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

from rest_framework import viewsets, mixins, filters
from rest_framework.decorators import detail_route
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.response import Response

from daiquiri.core.permissions import HasModelPermission
from daiquiri.core.paginations import ListPagination

from .models import Profile
from .utils import get_account_workflow
from .serializers import ProfileSerializer, GroupSerializer


class ProfileViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = (HasModelPermission, )

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = ListPagination

    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    ordering_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')

    @detail_route(methods=['put'], permission_classes=[HasModelPermission])
    def confirm(self, request, pk=None):
        if not get_account_workflow():
            raise MethodNotAllowed()

        profile = get_object_or_404(Profile, pk=pk)
        profile.confirm(request)
        return Response(self.get_serializer(profile).data)

    @detail_route(methods=['put'], permission_classes=[HasModelPermission])
    def activate(self, request, pk=None):
        if not get_account_workflow():
            raise MethodNotAllowed()

        profile = get_object_or_404(Profile, pk=pk)
        profile.activate(request)
        return Response(self.get_serializer(profile).data)

    @detail_route(methods=['put'], permission_classes=[HasModelPermission])
    def disable(self, request, pk=None):
        profile = get_object_or_404(Profile, pk=pk)
        profile.disable(request)
        return Response(self.get_serializer(profile).data)

    @detail_route(methods=['put'], permission_classes=[HasModelPermission])
    def enable(self, request, pk=None):
        profile = get_object_or_404(Profile, pk=pk)
        profile.enable(request)
        return Response(self.get_serializer(profile).data)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
