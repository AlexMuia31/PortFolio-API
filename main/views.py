from django.shortcuts import render
from main.serializers import AlexSerializer, JobSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from . models import *


class ExperienceList(ListCreateAPIView):
    serializer_class = AlexSerializer
    queryset = Alex.objects.all()


class JobsList(ListCreateAPIView):
    serializer_class = JobSerializer
    queryset = Jobs.objects.all()
