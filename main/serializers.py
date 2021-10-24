from .models import *
from rest_framework import serializers


class AlexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Alex
        fields = '__all__'


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jobs
        fields = '__all__'
