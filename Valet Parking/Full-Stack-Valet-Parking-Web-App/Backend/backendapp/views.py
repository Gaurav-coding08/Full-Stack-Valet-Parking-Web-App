from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from backendapp.serializers import Car_infoSerializer,Admin_infoSerializer
from backendapp.models import Car_info,Admin_info
from rest_framework.decorators import api_view
# Create your views here.

class car_info_create_api_view(APIView):

    def get_object(self, pk):
        cn =get_object_or_404(Car_info, Car_Number=pk)
        return cn

    def get(self, request, pk):
        sub= self.get_object(pk)
        serializer = Car_infoSerializer(sub)
        return Response(serializer.data)

    def post(self, request, pk):
        # sub = self.get_object(pk)
        serializer = Car_infoSerializer( data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        # car = self.get_object(pk)
        serializer = Car_infoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        car = self.get_object(pk)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class admin_info_create_api_view(APIView):

    def get_object(self, pk):
        cn =get_object_or_404(Admin_info, Email=pk)
        return cn

    def get(self, request, pk):
        sub= self.get_object(pk)
        serializer = Admin_infoSerializer(sub)
        return Response(serializer.data)

    def post(self, request, pk):
        # sub = self.get_object(pk)
        serializer = Admin_infoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        admin = self.get_object(pk)
        admin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET'])   
def getalladmininfo(request):
    admin_infos = Admin_info.objects.all()
    serializer = Admin_infoSerializer(admin_infos, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])   
def getallcarinfo(request):
    car_infos = Car_info.objects.all()
    serializer = Car_infoSerializer(car_infos, many=True)
    return Response(serializer.data)
    