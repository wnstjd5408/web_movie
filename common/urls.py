from django.urls import path

from . import views


app_name = 'common'

urlpatterns = [
    path('user_register/', views.user_register, name='user_register')

]
