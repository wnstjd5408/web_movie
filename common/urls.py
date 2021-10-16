from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'common'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:user_id>/', views.info, name='info'),
    path('update/', views.update, name='update'),
    path('profile_delete_view/', views.profile_delete_view,
         name='profile_delete_view'),
    path('change_password/', views.change_password, name='change'),
]
