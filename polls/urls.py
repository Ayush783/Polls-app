
from django.urls import path, include
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:question_id>/', views.details, name = 'details'),
    path('<int:question_id>/results', views.results, name = 'results'),
]