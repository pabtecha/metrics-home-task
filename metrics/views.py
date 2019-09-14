from django.db.models import Sum
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from metrics.filters import MetricsFilter
from metrics.models import Metrics
from metrics.serializers import MetricsSerializer


class MetricsViewSet(ViewSet):

    def list(self, request):
        f = MetricsFilter(request.GET, queryset=Metrics.objects.all())
        metrics = f.qs
        gruop_by = request.GET.get('group_by')
        if gruop_by:
            metrics = f.qs.values(gruop_by).annotate(impressions=Sum('impressions'),
                                                     clicks=Sum('clicks'),
                                                     installs=Sum('installs'),
                                                     spend=Sum('spend'),
                                                     revenue=Sum('revenue'))
        response_data = MetricsSerializer(instance=metrics, many=True).data
        return Response({"data": response_data}, status=status.HTTP_200_OK)
