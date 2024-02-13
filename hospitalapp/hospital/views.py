from rest_framework import viewsets, generics, status, parsers, permissions
from hospital import serializers
from hospital.models import Medication, User
from .perms import IsDoctor
from rest_framework.decorators import action
from rest_framework.response import Response

class MedicationViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Medication.objects.all()
    serializer_class = serializers.MedicationSerializer

class MedicationListCreate(generics.ListCreateAPIView):
    queryset = Medication.objects.all()
    serializer_class = serializers.MedicationSerializer
    permission_classes = [IsDoctor]

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True).all()
    serializer_class = serializers.UserSerializer
    # parser_classes = [parsers.MultiPartParser]

    def get_permissions(self):
        if self.action.__eq__('current_user'):
            return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get'], url_name='current-user', detail=False)
    def current_user(self, request):
        return Response(serializers.UserSerializer(request.user).data)
