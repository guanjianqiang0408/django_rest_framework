from django.contrib.auth.models import User, Group
from rest_framework import serializers


# 定义User模型数据序列化
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


# 定义Group模型数据序列化
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
