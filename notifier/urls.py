from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from notifications.views import NotificationViewSet, UserCreateView

router = DefaultRouter()
router.register(r"notifications", NotificationViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("register/", UserCreateView.as_view(), name="user-register"),
]
