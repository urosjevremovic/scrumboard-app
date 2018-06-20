from django.urls import path

from .api import ListApi, CardApi

urlpatterns = [
    path('lists/', ListApi.as_view(), name='list-api'),
    path('cards/', CardApi.as_view(), name='card-api'),
]