from django.test import TestCase

# Create your tests here.
from rest_framework import status

from metrics.models import Metrics


class MetricsViewSetTest(TestCase):

    def test_metrics_returns_200(self):
        res = self.client.get('/metrics')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_metrics_returns_elements(self):
        metric = Metrics(**{'date': '2017-05-17',
                            'channel': 'adcolony',
                            'country': 'US',
                            'os': 'android',
                            'impressions': '19887',
                            'clicks': '494',
                            'installs': '76',
                            'spend': '148.2',
                            'revenue': '149.04'})
        metric.save()

        res = self.client.get('/metrics')
        self.assertEqual(len(res.json()["data"]), 1)
