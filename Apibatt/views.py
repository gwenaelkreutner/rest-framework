from datetime import datetime

from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from Apibatt.serializers import UserSerializer, GroupSerializer, UserCustomSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

@api_view(['GET'])
def UserCustom(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    serializer = UserCustomSerializer(user, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def test(request):
    queryset = User.objects.all()
    serializer = UserSerializer(queryset, context={'request': request}, many=True)
    data = {'users': serializer.data,
            'date': datetime.now(),
            'test42': True
            }
    return Response(data)
