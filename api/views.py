from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer, AquariumSerializer, PHMeasurementSerializer, MeasurementSerializer, ParameterSerializer
from core.models import Aquarium, PHMeasurement, Measurement, Parameter

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class AquariumViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Aquarium.objects.all()
    serializer_class = AquariumSerializer

class PHMeasurementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = PHMeasurement.objects.all()
    serializer_class = PHMeasurementSerializer

class ParameterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer
    
class MeasurementViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
