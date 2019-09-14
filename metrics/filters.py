import django_filters

from metrics.models import Metrics


class MetricsFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    date_to = django_filters.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Metrics
        fields = ['country', "os", "channel"]
