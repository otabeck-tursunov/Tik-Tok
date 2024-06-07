from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token-refresh/', TokenRefreshView.as_view()),

    path('register/', RegisterView.as_view()),
    path('profile/details/', UserDetailsView.as_view()),
    path('profile/update/', UserUpdateView.as_view()),
    path('profile/delete/', UserDeleteView.as_view()),

    path('following/create/', FollowCreateView.as_view()),
    path('following/remove/<int:user_id>/', FollowRemoveView.as_view()),
    path('following/unfollow/<int:user_id>/', UnFollowView.as_view()),
]
