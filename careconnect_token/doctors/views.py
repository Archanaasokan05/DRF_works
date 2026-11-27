from django.shortcuts import get_object_or_404
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.
# API VIEWS for

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from doctors.serializers import DoctorSerializer
from doctors.models import Doctor

from doctors.permissions import IsAdminUserOrReadOnly
class DoctorListCreate(APIView):
    # local scope -->works only inside the block
    authentication_classes = [BasicAuthentication]      # username,password also send with the request
    permission_classes = [IsAdminUserOrReadOnly]

    # Reading all doctors
    def get(self,request):
        d=Doctor.objects.all()
        serializer_instance=DoctorSerializer(d,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    # Creating doctor
    def post(self,request):
        serializer_instance=DoctorSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


class DoctorRetrieveUpdateDelete(APIView):

    permission_classes = [IsAdminUserOrReadOnly]
    authentication_classes = [BasicAuthentication]  # username,password

    # Reading a specific doctor
    def get(self,request,pk):
        d=get_object_or_404(Doctor,id=pk)
        self.check_object_permissions(request,d)
        serializer_instance=DoctorSerializer(d)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    # Updating a doctor
    def put(self,request,pk):
        d=get_object_or_404(Doctor,id=pk)
        self.check_object_permissions(request,d)
        serializer_instance=DoctorSerializer(instance=d,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.data,status=status.HTTP_400_BAD_REQUEST)


    # Deleting a doctor
    def delete(self,request,pk):
        d=get_object_or_404(Doctor,id=pk)
        self.check_object_permissions(request,d)
        d.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# filtering doctors based on specialization
class DoctorFilter(APIView):
    def get(self,request):
        data=request.query_params.get('search')
        d=Doctor.objects.filter(specialization=data)
        serializer_instance=DoctorSerializer(d,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)


# APIView for creating admin user
from doctors.serializers import UserSerializer

class AdminRegister(APIView):
    def post(self,request):
        serializer_instance = UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)


