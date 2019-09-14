from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from metrics.providers import MetricsProvider
from metrics.serializers import MetricsSerializer, MetricQueryParamsRequestSerializer


class MetricsViewSet(ViewSet):
    metrics_provider = MetricsProvider()

    def list(self, request):
        query_params_serializer = MetricQueryParamsRequestSerializer(data=request.GET)
        query_params_serializer.is_valid(raise_exception=True)

        metrics = self.metrics_provider.list(filter_args=request.GET,
                                             group_by=query_params_serializer.validated_data.get('group_by'),
                                             order_by=query_params_serializer.validated_data.get('order_by'),
                                             order_type=query_params_serializer.validated_data.get('order_type'))

        response_data = MetricsSerializer(instance=metrics, many=True).data
        return Response({"data": response_data}, status=status.HTTP_200_OK)
