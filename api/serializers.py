from django.contrib.auth.models import User, Group
from rest_framework import serializers
from core.models import Aquarium, PHMeasurement, Measurement, Parameter


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class AquariumSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aquarium
        fields = ['aq_id', 'size', 'nickname', 'startDate']
        
class ParameterSerializer(serializers.HyperlinkedModelSerializer):    
#    aq = serializers.HyperlinkedIdentityField(view_name='aquarium-detail', read_only=False)

    class Meta:
        model = Parameter
        fields = ['param_id', 'p_order', 'aq_id', 'name', 'units']
        
class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Measurement
        fields = ['measure_id', 'param_id', 'value', 'time']
        
class PHMeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PHMeasurement
        fields = ['aquarium', 'measurement', 'measure_time']
