from django.urls import path

from . import views

urlpatterns = [
    path('', views.endpoints),
    path('advocates/', views.advocates, name='advocates'),
    path('advocates/<str:username>/', views.Advocate_detail.as_view(), name='advocate_detail')
]
