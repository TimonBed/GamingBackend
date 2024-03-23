# urls.py

from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import IsAuthenticatedView, GetCurrentUserView, UserViewSet, send_email

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('is-authenticated/', IsAuthenticatedView.as_view(),
         name='is_authenticated'),
    path('get-current-user/', GetCurrentUserView.as_view(), name='get_current_user'),
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create',
         'put': 'update', 'delete': 'destroy'}), name='users'),
    path('users/<int:pk>/', UserViewSet.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
    path('send-email/', send_email, name='send_email'),
]
