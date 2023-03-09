from django.urls import path
from .views import RegisterAPIView, LoginAPIView, LogoutAPIView, ProfileAPIView, AddressAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('profile/<int:pk>/', ProfileAPIView.as_view()),
    path('<int:id>/addresses/', AddressAPIView.as_view()),
]