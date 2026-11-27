from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from events.serializers import EventSerializer
from events.permissions import IsOrganizerOrReadOnly
from events.models import Event

# Create your views here.

class EventListCreate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOrganizerOrReadOnly]
    def get(self,request):
        if request.user.role=='customer':
            e=Event.objects.all()   #if customer reads all records
        else:
            e=Event.objects.filter(organizer=request.user)  #if organizer only their own records
        serializer_instance= EventSerializer(e,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer_instance= EventSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(organizer=request.user)
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


class EventRetrieveUpdateDelete(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsOrganizerOrReadOnly]
    def get(self,request,pk):
        if request.user.role=='customer':
            event=get_object_or_404(Event,id=pk)
        else:
            event=get_object_or_404(Event,id=pk,organizer=request.user)
        serializer_instance= EventSerializer(event)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        event=get_object_or_404(Event,id=pk)
        self.check_object_permissions(request,event)
        serializer_instance=EventSerializer(instance=event,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        e=get_object_or_404(Event,id=pk)
        self.check_object_permissions(request,e)
        e.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

