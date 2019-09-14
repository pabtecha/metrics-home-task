from django.db.models import Sum

from metrics.models import Metrics
from metrics.filters import MetricsFilter


class MetricsProvider:
    queryset = Metrics.objects.all()

    def list(self, filter_args: dict, group_by: str = None):
        list_queryset = self.get_filtered_queryset(filter_args)

        if group_by:
            list_queryset = self.group_by_queryset(list_queryset, group_by)

        return list_queryset

    def get_filtered_queryset(self, filter_args: dict):
        return MetricsFilter(filter_args, queryset=self.queryset).qs

    @staticmethod
    def group_by_queryset(queryset, group_by_field: str):
        return queryset.values(group_by_field).annotate(impressions=Sum('impressions'),
                                                        clicks=Sum('clicks'),
                                                        installs=Sum('installs'),
                                                        spend=Sum('spend'),
                                                        revenue=Sum('revenue'))
