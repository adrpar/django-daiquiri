from daiquiri.uws.viewsets import UWSViewSet

from .models import Job
from .serializers import JobsSerializer, JobSerializer


class JobsViewSet(UWSViewSet):
    queryset = Job.objects.all()
    list_serializer_class = JobsSerializer
    detail_serializer_class = JobSerializer


class QueryJobsViewSet(JobsViewSet):
    detail_url_name = 'uws:query-detail'
    job_type = Job.JOB_TYPE_QUERY
