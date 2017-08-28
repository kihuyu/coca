# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datacollections.models import Datacollection
from datacollections.serializers import DatacollectionSerializer
from django.contrib.auth.models import User
from datacollections.serializers import UserSerializer
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from datacollections.permissions import IsOwner


@api_view(['GET', 'POST'])
def datacollection_list(request, format=None):
    """
    List all datacollections, or create a new datacollection.
    """
    if request.method == 'GET':
        datacollections = Datacollection.objects.all()
        serializer = DatacollectionSerializer(datacollections, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DatacollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    permission_classes = (permissions.IsAuthenticated,)

@api_view(['GET', 'PUT', 'DELETE'])
def datacollection_detail(request, pk, format=None):
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    """
    Retrieve, update or delete a data collection instance.
    """
    try:
        datacollection = Datacollection.objects.get(pk=pk)
    except Datacollection.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DatacollectionSerializer(datacollection)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DatacollectionSerializer(datacollection, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        datacollection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def user_list(request, format=None):
        if request.method == 'GET':
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = UserSerializer(user)
            return Response(serializer.data)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'datacollections': reverse('datacollection-list', request=request, format=format)
    })
