import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    JOBTitle = django_filters.CharFilter(lookup_expr='icontains')
    JOBDescription = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Job
        fields = '__all__'
        exclude = ['JOBowner', 'JOBDescription', 'JOBImage', 'JOBSlug', 'JOBCreated_at', 'JOBVacancy']
