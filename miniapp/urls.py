from django.urls import path
from .views import InfoListCreate, PhrasesListCreate

from miniapp import views

urlpatterns = [
    path('api/infos/', InfoListCreate.as_view(), name='Info-list-create'),
    path('api/phrases/', PhrasesListCreate.as_view(), name='Phrases-list-create'),
    path('info/', views.info_list, name='info_list'),  
    path('info/<int:pk>/', views.info_detail, name='info_detail'),  # Страница с деталями
    path('', views.app_view, name='app'),  # Главная страница
    path('information/', views.information_view, name='information'),  # Страница с информацией
    path('map/', views.map_view, name='map'),
    path('phrases/', views.phrases_list, name='phrases_list'),
    path('phrases/<int:pk>/', views.phrases_detail, name='phrases_detail'),
]