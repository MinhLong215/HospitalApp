
from django.urls import path, include
from rest_framework import routers
from hospital import views

router = routers.DefaultRouter()
router.register('medications', views.MedicationViewSet, basename='medications')

urlpatterns = [
    path('', include(router.urls)),
]
