from django.urls import path

from . import views

app_name = 'core'
urlpatterns = [
    # ex: /core/
    path('', views.index, name='index'),
    # ex: /core/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
#    path('<int:aquarium_id>/', views.detail, name='detail'),
]
