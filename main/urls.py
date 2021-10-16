from django.urls import path

from . import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('reservation/', views.reservation, name='reservation'),
]
