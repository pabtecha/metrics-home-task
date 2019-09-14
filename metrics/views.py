from django.db.models import Sum
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from metrics.providers import MetricsProvider
from metrics.serializers import MetricsSerializer, MetricGroupByRequestSerializer


class MetricsViewSet(ViewSet):
    metrics_provider = MetricsProvider()

    def list(self, request):
        group_by_serializer = MetricGroupByRequestSerializer(data=request.GET)
        group_by_serializer.is_valid(raise_exception=True)

        group_by_fields = group_by_serializer.validated_data.get('group_by')
        order_by_field = request.GET.get('order_by')

        metrics = self.metrics_provider.list(request.GET, group_by_fields, order_by_field)

        response_data = MetricsSerializer(instance=metrics, many=True).data
        return Response({"data": response_data}, status=status.HTTP_200_OK)
