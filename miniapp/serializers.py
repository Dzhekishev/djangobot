from rest_framework import serializers
from .models import Info, Phrases

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['id', 'name', 'description', 'image']

class PhrasesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Phrases
        fields=['id','name','words','image']
