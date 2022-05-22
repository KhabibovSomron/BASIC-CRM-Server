from rest_framework import serializers
from .models import Customer, Position, Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id', 'title', 'code')


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'title')


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('fullName', 'country', 'position', 'email', 'companyName')


class CustomerListSerializer(serializers.ModelSerializer):
    country = serializers.SlugRelatedField(slug_field="title", read_only=True)
    position = serializers.SlugRelatedField(slug_field="title", read_only=True)
    class Meta:
        model = Customer
        fields = ('id', 'fullName', 'country', 'position', 'email', 'companyName')