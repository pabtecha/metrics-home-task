from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet


class MetricsViewSet(ViewSet):

    def list(self, request):
        return Response(status=status.HTTP_200_OK)
