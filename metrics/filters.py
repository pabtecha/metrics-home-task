import django_filters

from metrics.models import Metrics


class MetricsFilter(django_filters.FilterSet):
    class Meta:
        model = Metrics
        fields = ['country', "os", "channel"]
