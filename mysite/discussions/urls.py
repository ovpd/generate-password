from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.discussions_main, name = 'discussions')
]
