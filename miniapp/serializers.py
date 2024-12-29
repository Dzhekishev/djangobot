from rest_framework import serializers
from .models import*
from django import forms

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['id', 'name', 'description', 'image']

class PhrasesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Phrases
        fields=['id','name','words','image']

class RouteSerializer(serializers.ModelSerializer):
    info = serializers.PrimaryKeyRelatedField(queryset=Info.objects.all(), many=True)

    class Meta:
        model = Route
        fields = ['id', 'name', 'image', 'info']


class MapsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Maps
        fields=['id','name','image','site']