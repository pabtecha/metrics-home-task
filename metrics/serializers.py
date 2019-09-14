from rest_framework import serializers

from metrics.models import Metrics


class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        fields = '__all__'
        extra_kwargs = {
            'date': {'required': False},
            'country': {'required': False},
            'channel': {'required': False},
            'os': {'required': False},
        }
