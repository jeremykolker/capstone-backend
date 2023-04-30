from rest_framework import serializers 
from .models import Item

class ItemSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Item # tell django which model to use
        fields = ('id', 'photo_url', 'name', 'color', 'price', 'size', 'description')