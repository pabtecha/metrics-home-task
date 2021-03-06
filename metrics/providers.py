from django.db.models import Sum, F

from metrics.enumerations import OrderByTypes
from metrics.models import Metrics
from metrics.filters import MetricsFilter


class MetricsProvider:
    queryset = Metrics.objects.all()

    def list(self, filter_args: dict, group_by: list = None, order_by: str = None, order_type: str= None):
        list_queryset = self.get_filtered_queryset(filter_args)

        if group_by:
            list_queryset = self.group_by_queryset(list_queryset, group_by)

        if order_by:
            list_queryset = self.order_queryset(list_queryset, order_by, order_type)

        return list_queryset

    def get_filtered_queryset(self, filter_args: dict):
        return MetricsFilter(filter_args, queryset=self.queryset).qs

    @staticmethod
    def group_by_queryset(queryset, fields: list):
        return queryset.values(*fields).annotate(impressions=Sum('impressions'),
                                                 clicks=Sum('clicks'),
                                                 installs=Sum('installs'),
                                                 spend=Sum('spend'),
                                                 revenue=Sum('revenue'),
                                                 cpi=F('spend') / F('revenue'))

    @staticmethod
    def order_queryset(queryset, field: str, type: str):
        if type and type == OrderByTypes.DESC:
            field = '-{}'.format(field)
        return queryset.order_by(field)
