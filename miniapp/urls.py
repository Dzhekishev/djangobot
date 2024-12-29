from django.urls import path
from .views import*

from miniapp import views

urlpatterns = [
    path('api/infos/', InfoListCreate.as_view(), name='Info-list-create'),
    path('api/phrases/', PhrasesListCreate.as_view(), name='Phrases-list-create'),
    path('infos/<int:route_id>/', views.info_list, name='info_list'),
    path('info/<int:pk>/', views.info_detail, name='info_detail'),
    path('', views.app_view, name='app'),  # Главная страница
    #path('map/', views.map_view, name='map'),
    path('phrases/', views.phrases_list, name='phrases_list'),
    path('phrases/<int:pk>/', views.phrases_detail, name='phrases_detail'),
    path('routes/', views.routes_list, name='routes_list'),
    path('routes/<int:pk>/', views.routes_detail, name='routes_detail'),
    path('api/route/', RouteListCreate.as_view(), name='Route-list-create'),
    path('api/maps/',MapsListCreate.as_view(),name='Maps-List-create'),
    path('maps/',views.maps_list,name='maps_list'),
]