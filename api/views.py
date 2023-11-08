from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from core.models import Product
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import generics


class ProductView(APIView):
    def get(self,request,id):
        product=Product.objects.get(id=id)
        serializers=ProductGetSerializers(product,many=True,context={'request': request})
        return Response(serializers.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializers=ProductPostSerializers(data=request.data,context={'request': request})
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
        
class ProductDetailApiView(APIView):
    def get(self,request,id):
        # Product=Product.objects.get(id=id)
        # serializers=ProductGetSerializers(Product,context={'request':request})
        # return Response(serializers.data,status=status.HTTP_200_OK)
        try:
            product=Product.objects.get(id=id)
            serializers=ProductGetSerializers(product,context={'request':request})
            return Response(serializers.data,status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,data={'message':'News not found '})
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR,data={'message': 'Internal server error'})
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST,data={'message': 'Invalid id'})
        
    def put(self,request,id):
        try:
            product=Product.objects.get(id=id)
            serializers=ProductGetSerializers(product,data=request.data,context={'request': request})
            if serializers.is_valid():
                serializers.save()
                return Response (serializers.data,status=status.HTTP_200_OK)
            else:
                return Response (serializers.errors,status=status.HTTP_400_BAD_REQUEST) 

        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND,data={'message': 'Product not found'})
    
    def delete(self,request,id):
        try:
            product=Product.objects.get(id=id)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT,data={'message': 'Product deleted'})
        except Product.DoesNotExist:
            return Response (status=status.HTTP_404_NOT_FOUND,data={'message': 'Product not found'})

    
class SubsciberApiView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = SubscriberSerializer(data = request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)