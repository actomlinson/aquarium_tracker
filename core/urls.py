from django.urls import path

from . import views

urlpatterns = [
    # ex: /core/
    path('', views.index, name='index'),
    # ex: /core/5/
    path('<int:aquarium_id>/', views.detail, name='detail'),
]
