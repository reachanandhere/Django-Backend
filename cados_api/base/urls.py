from django.urls import path

from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
#    TokenRefreshView, 
)

urlpatterns = [
    path('', views.endpoints),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('advocates/', views.advocates, name='advocates'),
    path('advocates/<str:username>/', views.Advocate_detail.as_view(), name='advocate_detail'),
    path('companies/', views.companies_list, name='companies'),
]
