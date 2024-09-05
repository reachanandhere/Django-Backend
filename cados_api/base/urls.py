from django.urls import path

from .views import endpoints, advocates, advocate_detail

urlpatterns = [
    path('', endpoints),
    path('advocates/', advocates, name='advocates'),
    path('advocates/<str:username>/', advocate_detail),
]
