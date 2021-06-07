from django.conf.urls import include, url
from django.urls import path
from rest_framework import routers

from Apibatt import views

# Create a router and register our viewsets with it.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    path('users/<int:pk>/permissions', views.UserCustom),
    path('test/test1', views.test),
]
