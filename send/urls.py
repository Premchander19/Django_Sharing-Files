from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('send/', views.send, name='send'),
    path('receive/', views.receive, name='receive'),
    path('download/', views.download, name='download'),
    path('upload/', views.upload, name='upload')

]
