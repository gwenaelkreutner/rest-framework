from django.contrib.auth.models import User, Group
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCustomSerializer(serializers.ModelSerializer):
    # Utilise seulement le __str__ de l'objet
    # groups = serializers.StringRelatedField(many=True)
    # Appelle l'objet dans sa globalité
    groups = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'groups']
