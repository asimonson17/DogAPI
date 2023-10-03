"""
URL configuration for DogAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from dogs import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'dogs', views.DogViewSet)
router.register(r'breeds', views.BreedViewSet)

urlpatterns = [
    path('dogs/', views.DogList.as_view()),
    path('dogs/<int:pk>/', views.DogDetail.as_view()),
    path('dogs/', views.BreedList.as_view()),
    path('dogs/<int:pk>/', views.BreedDetail.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

urlpatterns = format_suffix_patterns(urlpatterns)
