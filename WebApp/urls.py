from django.urls import path
from . import views

app_name = 'WebApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('MachineLearning/RPS', views.ML_RPS, name='ml-rps'),
    path('MachineLearning/TTT', views.ML_TTT, name='ml-ttt'),
]