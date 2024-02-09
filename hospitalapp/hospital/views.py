from rest_framework import viewsets, generics
from hospital import serializers
from hospital.models import Medication
from .perms import IsDoctor

class MedicationViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Medication.objects.all()
    serializer_class = serializers.MedicationSerializer

class MedicationListCreate(generics.ListCreateAPIView):
    queryset = Medication.objects.all()
    serializer_class = serializers.MedicationSerializer
    permission_classes = [IsDoctor]

