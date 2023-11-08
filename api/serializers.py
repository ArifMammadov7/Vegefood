from rest_framework import serializers
from core.models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields=['id','title']


class ProductGetSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['title','content','image','category','created_at']


class ProductPostSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['title','content','image','category']

class SubscriberSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = Subscriber
        fields = ['email',]