from django.shortcuts import render
from rest_framework.decorators import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

class EntryAPI(APIView):
    def get(self,request):
        objectsmain=Entry.objects.all()
        serializer=EntrySerializers(objectsmain,many=True)
        return Response({'status':200,'message':serializer.data})
    
    def post(self,request):
        data=request.data
        serializer=EntrySerializers(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
        serializer.save()
        return Response({'status':200,'message':serializer.data})
    
    def put(self,request):
        try:
            objectsmain=Entry.objects.get(id=request.data['id'])
            serializer=EntrySerializers(objectsmain,data=request.data,partial=False)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':200,'message':serializer.errors})
            serializer.save()
            return Response({'status':200,'message':serializer.data})
        
        except Exception as ex:
            print(ex)
            return Response({'status':200,'message':'invalid id'})
    
    def patch(self,request):
        try:
            objectsmain=Entry.objects.get(id=request.data['id'])
            serializer=EntrySerializers(objectsmain,data=request.data,partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':200,'message':serializer.errors})
            serializer.save()
            return Response({'status':200,'message':serializer.data})
        
        except Exception as ex:
            print(ex)
            return Response({'status':200,'message':'invalid id'})
    
    def delete(self,request):
        try:
            id=request.data['id']
            print(id)
            objectsmain=Entry.objects.get(id=id)
            objectsmain.delete()
            return Response({'status':200,'message':'deleted'})
        
        except Exception as ex:
            print(ex)
            return Response({'status':200,'message':'invalid id'})
