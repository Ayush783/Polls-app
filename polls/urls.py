
from django.urls import path, include
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('recent/', views.recent, name = 'recent-polls'),
    path('<int:question_id>/', views.details, name = 'details'),
    path('<int:question_id>/results', views.results, name = 'results'),
    path('<int:question_id>/vote', views.vote, name = 'vote'),
    path('create/', views.create, name = 'create-poll'),
]