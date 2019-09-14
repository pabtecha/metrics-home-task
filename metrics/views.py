from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from metrics.models import Metrics
from metrics.serializers import MetricsSerializer


class MetricsViewSet(ViewSet):

    def list(self, request):
        response_data = MetricsSerializer(instance=Metrics.objects.all(), many=True).data
        return Response({"data": response_data}, status=status.HTTP_200_OK)
