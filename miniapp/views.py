from django.shortcuts import render,get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import*
from .serializers import*

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

class RouteListCreate(APIView):
    def get(self, request):
        route = Route.objects.all()
        serializer = RouteSerializer(route, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RouteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MapsListCreate(APIView):
    def get(self, request):
        maps = Maps.objects.all()
        serializer = MapsSerializer(maps, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MapsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def maps_list(request):
    maps = Maps.objects.all()  # Получаем все объекты из базы данных
    return render(request, 'miniapp/maps_list.html', {'maps': maps})



def phrases_list(request):
    phrases = Phrases.objects.all()  # Получаем все объекты из базы данных
    return render(request, 'miniapp/phrases_list.html', {'phrases': phrases})

def phrases_detail(request, pk):
    phrase = Phrases.objects.get(pk=pk)  # Получаем информацию по id
    return render(request, 'miniapp/phrases_detail.html', {'phrase': phrase})



def info_list(request, route_id):
    route = get_object_or_404(Route, id=route_id)  # Получаем маршрут по ID
    infos = route.info.all()  # Фильтруем связанные объекты Info через ManyToManyField
    return render(request, 'miniapp/info_list.html', {'infos': infos})

def info_detail(request, pk):
    info = get_object_or_404(Info, pk=pk)
    # Получаем ID маршрута, связанного с этим Info
    route = info.route_set.first()  # Если `ManyToMany`, берем первый связанный Route
    route_id = route.id if route else None  # Проверяем, связан ли Info с Route
    return render(request, 'miniapp/info_detail.html', {'info': info, 'route_id': route_id})

def routes_list(request):
    route = Route.objects.all()  # Получаем все объекты из базы данных
    return render(request, 'miniapp/routes_list.html', {'route': route})

def routes_detail(request, pk):
    route = Route.objects.get(pk=pk)  # Получаем информацию по id
    return render(request, 'miniapp/routes_detail.html', {'route': route})



def app_view(request):
    return render(request, 'miniapp/app.html')

'''def information_view(request):
    return render(request, 'miniapp/information.html')
'''
def map_view(request):
    return render(request, 'miniapp/maps.html')