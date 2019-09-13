from django.urls import path, include
from rest_framework.routers import DefaultRouter
from metrics import views as metrics_views

router = DefaultRouter(trailing_slash=False)
router.register(r'metrics', metrics_views.MetricsViewSet, basename='metrics')

urlpatterns = [
    path('', include(router.urls)),
]