from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bookings.serializers import BookingSerializer
from bookings.models import Booking

# Create your views here.

class BookingListCreate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer_instance = BookingSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request):
    # #     if request.user.role == 'customer':
    #     b = Booking.objects.all()  # if customer reads all records
    # #     else:
    # #         e = Event.objects.filter(organizer=request.user)  # if organizer only their own records
    #     serializer_instance = BookingSerializer(b, many=True)
    #     return Response(serializer_instance.data, status=status.HTTP_200_OK)

class BookingRetrieveUpdateDelete(APIView):
    pass