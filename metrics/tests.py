from django.test import TestCase

# Create your tests here.
from rest_framework import status

from metrics.models import Metrics

metrics_json = [
    {'date': '2017-05-17',
     'channel': 'adcolony',
     'country': 'US',
     'os': 'android',
     'impressions': '19887',
     'clicks': '494',
     'installs': '76',
     'spend': '148.2',
     'revenue': '149.04'},
    {'date': '2017-05-17',
     'channel': 'adcolony',
     'country': 'ES',
     'os': 'android',
     'impressions': '19887',
     'clicks': '494',
     'installs': '76',
     'spend': '148.2',
     'revenue': '149.04'}
]


class MetricsViewSetTest(TestCase):

    def test_metrics_returns_200(self):
        res = self.client.get('/metrics')
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_metrics_returns_elements(self):
        metric = Metrics(**metrics_json[0])
        metric.save()

        res = self.client.get('/metrics')
        self.assertEqual(len(res.json()["data"]), 1)

    def test_metrics_with_field_filter_returns_filtered_elements(self):
        metric = Metrics(**metrics_json[0])
        metric.save()
        metric2 = Metrics(**metrics_json[1])
        metric2.save()

        res = self.client.get('/metrics', params={"country": "US"})
        self.assertEqual(len(res.json()["data"]), 1)
