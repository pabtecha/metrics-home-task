from django.test import TestCase

# Create your tests here.
from rest_framework import status


class MetricsViewSetTest(TestCase):

    def test_metrics_returns_200(self):
        res = self.client.get('/metrics')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
