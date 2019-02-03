from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from notifications.views import TemplateViewSet

router = DefaultRouter()
router.register(r'templates', TemplateViewSet, 'templates')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
