from rest_framework import serializers

from metrics.enumerations import ORDER_BY_CHOICES, OrderByTypes, GROUP_BY_CHOICES
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


class MetricQueryParamsRequestSerializer(serializers.Serializer):
    group_by = serializers.CharField(required=False)
    order_by = serializers.ChoiceField(required=False, choices=ORDER_BY_CHOICES)
    order_type = serializers.ChoiceField(required=False, choices=OrderByTypes.choices())

    def validate_group_by(self, value):
        if value:
            try:
                fields = value.split(';')
            except Exception:
                raise serializers.ValidationError("Not a valid field format. Please separate values with ;")

            if any(map(lambda x: x not in GROUP_BY_CHOICES, fields)):
                raise serializers.ValidationError("Not a valid field value. "
                                                  f"Options are {GROUP_BY_CHOICES}")

            return fields

        return value
