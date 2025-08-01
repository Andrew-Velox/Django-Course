from django.shortcuts import render
from rest_framework import viewsets

from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly



class DoctorViewset(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer

class DesignationViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer

class SpecializationViewset(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer

class AvailableTimeViewset(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer

class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

