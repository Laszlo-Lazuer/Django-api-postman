from django.urls import path, include
from . import views
from rest_framework import routers # allows get/post requests

router = routers.DefaultRouter()
router.register('courses', views.CourseView)

urlpatterns = [
    path("", include(router.urls)),
]
