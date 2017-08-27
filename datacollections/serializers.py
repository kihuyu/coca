from rest_framework import serializers
from datacollections.models import Datacollection
from django.contrib.auth.models import User


class DatacollectionSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Datacollection
        fields = ('id', 'name', 'latitude', 'longitude', 'favourite_drink', 'date_of_collection', 'owner')

class UserSerializer(serializers.ModelSerializer):
    datacollections = serializers.PrimaryKeyRelatedField(many=True, queryset=Datacollection.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'datacollections')
