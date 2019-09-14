from rest_framework import serializers

from metrics.models import Metrics


class MetricsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrics
        exclude = ['id']
        extra_kwargs = {
            'date': {'required': False},
            'country': {'required': False},
            'channel': {'required': False},
            'os': {'required': False},
        }


class MetricGroupByRequestSerializer(serializers.Serializer):
    CHOICES = ('date', 'country', 'channel', 'os')
    group_by = serializers.CharField(required=False)

    def validate_group_by(self, value):
        if value:
            try:
                fields = value.split(';')
            except Exception:
                raise serializers.ValidationError("Not a valid field format. Please separate values with ;")

            if any(map(lambda x: x not in MetricGroupByRequestSerializer.CHOICES, fields)):
                raise serializers.ValidationError("Not a valid field value. "
                                                  f"Options are {MetricGroupByRequestSerializer.CHOICES}")

            return fields

        return value
