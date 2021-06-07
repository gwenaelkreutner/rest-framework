from django.conf.urls import url
from django.urls import include, path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'api/', include('Apibatt.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]