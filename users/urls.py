from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.views import UserCreateApiView, PaymentsListAPIView, PaymentCreateAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path("register/", UserCreateApiView.as_view(), name="register"),
    path(
        "token/",
        TokenObtainPairView.as_view(permission_classes=[AllowAny]),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh/",
        TokenRefreshView.as_view(permission_classes=[AllowAny]),
        name="token_refresh",
    ),
    path("payments/", PaymentsListAPIView.as_view(), name="payments_list"),
    path("payment/", PaymentCreateAPIView.as_view(), name="payment"),
]
