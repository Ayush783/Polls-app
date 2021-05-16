
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:question_id>/', views.details, name = 'details'),
    path('<int:question_id>/results', views.results, name = 'results'),
]