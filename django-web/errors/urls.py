from django.urls import path
from . import views

urlpatterns = [
    path('400',views.error_400,name='400'),
    path('401',views.error_401,name='401'),
    path('403',views.error_403,name='403'),
    ]
