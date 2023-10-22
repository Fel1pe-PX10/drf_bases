from django.contrib import admin
from django.urls import path, re_path, include


from . import views

app_name = 'personas_app'

urlpatterns = [
    path('api/persona/list/', views.PersonListApiView.as_view(),),
    path('api/persona/create/', views.PersonCreateApiView.as_view(),),
    path('api/persona/detail/<pk>', views.PersonDetailApiView.as_view(),),
    path('api/persona/delete/<pk>', views.PersonDeleteApiView.as_view(),),
    path('api/persona/update/<pk>', views.PersonUpdateApiView.as_view(),),
]