from django.urls import path
from . import views

urlpatterns=[
    path('', views.redirigir),
    path('time_display',views.index)

]