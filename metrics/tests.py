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
    {'date': '2017-08-17',
     'channel': 'adcolony',
     'country': 'ES',
     'os': 'android',
     'impressions': '19887',
     'clicks': '494',
     'installs': '76',
     'spend': '148.2',
     'revenue': '149.04'},
    {'date': '2017-09-17',
     'channel': 'adcolony',
     'country': 'US',
     'os': 'ios',
     'impressions': '19887',
     'clicks': '494',
     'installs': '76',
     'spend': '148.2',
     'revenue': '149.04'},
    {'date': '2017-05-16',
     'channel': 'unityads',
     'country': 'US',
     'os': 'ios',
     'impressions': '19887',
     'clicks': '494',
     'installs': '76',
     'spend': '148.2',
     'revenue': '149.04'},
]


class MetricsViewSetTest(TestCase):
    metrics_url = '/metrics'
    @classmethod
    def setUpTestData(cls):
        metrics = [Metrics(**row) for row in metrics_json]
        Metrics.objects.bulk_create(metrics)

    def test_list_returns_200(self):
        res = self.client.get(self.metrics_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_list_returns_all_elements(self):
        res = self.client.get(self.metrics_url)
        self.assertEqual(len(res.json()["data"]), len(metrics_json))

    def test_list_with_field_filter_returns_filtered_elements(self):
        res = self.client.get(self.metrics_url, {"country": "ES"})
        self.assertEqual(len(res.json()["data"]), 1)

    def test_list_with_multiple_fields_filter_returns_filtered_elements(self):
        params = {"country": "US", "os": "android", "channels": "unityads"}

        res = self.client.get(self.metrics_url, params)
        self.assertEqual(len(res.json()["data"]), 1)

    def test_list_with_same_day_date_range_filter_returns_filtered_elements(self):
        params = {"date_from": "2017-08-17", "date_to": "2017-08-17"}

        res = self.client.get(self.metrics_url, params)
        self.assertEqual(len(res.json()["data"]), 1)

    def test_list_with_date_range_filter_returns_filtered_elements(self):
        params = {"date_from": "2017-05-15", "date_to": "2017-05-17"}

        res = self.client.get(self.metrics_url, params)
        self.assertEqual(len(res.json()["data"]), 2)

    def test_list_with_group_by_single_field_returns_grouped_elements(self):
        params = {"group_by": "country"}
        res = self.client.get(self.metrics_url, params)
        self.assertEqual(len(res.json()["data"]), 2)
