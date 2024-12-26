from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Info, Phrases
from .serializers import InfoSerializer, PhrasesSerializer

class InfoListCreate(APIView):
    def get(self, request):
        infos = Info.objects.all()
        serializer = InfoSerializer(infos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhrasesListCreate(APIView):
    def get(self, request):
        phrases = Phrases.objects.all()
        serializer = PhrasesSerializer(phrases, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PhrasesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def phrases_list(request):
    phrases = Phrases.objects.all()  # Получаем все объекты из базы данных
    return render(request, 'miniapp/phrases_list.html', {'phrases': phrases})

def phrases_detail(request, pk):
    phrase = Phrases.objects.get(pk=pk)  # Получаем информацию по id
    return render(request, 'miniapp/phrases_detail.html', {'phrase': phrase})



def info_list(request):
    infos = Info.objects.all()  # Получаем все объекты из базы данных
    return render(request, 'miniapp/info_list.html', {'infos': infos})


def info_detail(request, pk):
    info = Info.objects.get(pk=pk)  # Получаем информацию по id
    return render(request, 'miniapp/info_detail.html', {'info': info})


def app_view(request):
    return render(request, 'miniapp/app.html')

def information_view(request):
    return render(request, 'miniapp/information.html')

def map_view(request):
    return render(request, 'miniapp/maps.html')