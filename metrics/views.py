from django.db.models import Sum
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from metrics.providers import MetricsProvider
from metrics.serializers import MetricsSerializer


class MetricsViewSet(ViewSet):
    metrics_provider = MetricsProvider()

    def list(self, request):
        metrics = self.metrics_provider.list(request.GET, request.GET.get('group_by'))

        response_data = MetricsSerializer(instance=metrics, many=True).data
        return Response({"data": response_data}, status=status.HTTP_200_OK)
