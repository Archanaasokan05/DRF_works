from django.shortcuts import get_object_or_404
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

# Create your views here.
# API VIEWS for

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, authentication
from doctors.models import Doctor
 # Appointment create view

from patients.serializers import AppointmentSerializer
from patients.models import Appointment
from datetime import time, datetime, timedelta


class AppointmentCreate(APIView):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]  # only authenticated users can create appointment
    def post(self,request):
        serializer_instance = AppointmentSerializer(data=request.data)
        if serializer_instance.is_valid():
            # Token number
            data=serializer_instance.validated_data     #data after validation
            d=data['doctor'] #fetches doctor from client data
            date=data['appointment_date']   #fetches date from client data
            token=0
            appointment_time=time(9,0)
            print(appointment_time)
            # find the doctor appointments on that particular date using filter query
            a=Appointment.objects.filter(doctor=d,appointment_date=date).last()     #find the last record
            if a:   #if found
                token=a.token_number+1
                appointment_time=datetime.combine(date,a.appointment_time)+timedelta(minutes=15).time()
            else:   #if no record
                token=1

            # appointment time

            serializer_instance.save(token_number=token,appointment_time=appointment_time)
            response={"status":"Booking Confirmed Successfully",
                      "booking_data":serializer_instance.data}

            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

# APIView for creating a user
from patients.serializers import PatientSerializer

class PatientRegister(APIView):
    def post(self,request):
        serializer_instance = PatientSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)

# model(default-User)
# serializer
# view
# url path


from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
# class obtain_auth_token(APIView):
#     def post(self,request):
#         # fetches username and password from user data
#         u=request.data['username']
#         p=request.data['password']
#
#         # Checks whether matching user exists in User table
#         user=authenticate(username=u,password=p)
#             # authenticate() checks whether user exists or not
#             # if matching user exists it returns user object
#             # else none
#         # if user exists
#         if user:
#             # generates token and sends as Response
#             token,created=Token.objects.get_or_create(user=user)
#             print(token,created)
#             return Response({'token':token.key},status=status.HTTP_201_CREATED)
#         # else
#         else:
#             # sends Response as Invalid User Credentials
#             return Response({'message': 'Invalid Credentials,Unable to login'}, status=status.HTTP_400_BAD_REQUEST)
