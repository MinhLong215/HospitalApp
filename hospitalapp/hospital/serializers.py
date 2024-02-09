from hospital.models import Medication, Prescription
from rest_framework import serializers

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'