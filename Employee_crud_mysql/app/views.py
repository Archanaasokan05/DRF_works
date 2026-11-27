# from django.db.models import Model
# from django.views import View
# from rest_framework import response
# from app import serializers
# from django.http import JsonResponse
# from json import loads
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import csrf_exempt

# ----------------------------------DRF-------------------------------


from django.shortcuts import render, get_object_or_404
from app.models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers import EmployeeSerializer


# APIView for reading all records
class EmployeeList(APIView):
    def get(self,request):
        #reads all employee records from Employee table
        e=Employee.objects.all()        #django format qs
        #converts the qs into python native using EmployeeSerializer
        serializer_instance=EmployeeSerializer(e,many=True)
        print(serializer_instance.data)
        return Response(serializer_instance.data)


# # APIView for creating a new record
class EmployeeCreate(APIView):                  # serializers used for conversion and validation
    def post(self,request):
        # data=request.data       #python native

        #validation+conversion(native to model object
        serializers_instance=EmployeeSerializer(data=request.data)
        print(request.data)

        #checks whether the data coming from client is valid,if valid saves the data into model
        if serializers_instance.is_valid():
            serializers_instance.save()             #save the data into model
            return Response(serializers_instance.data)      #sends created object as response

        #if data is not valid it shows the error
        else:
            return Response(serializers_instance.errors)


# # APIView for reading a specific employee record
class EmployeeDetail(APIView):
    def get(self,request,i):
        # reads employee record matching id
        # e=Employee.objects.get(id=i)      #shows error if id is not in the table,to fix that given code is used(get_object_or_404)
        e=get_object_or_404(Employee,id=i)
        # calls Employee Serializer class for serialization
        serializer_instance=EmployeeSerializer(e)
        # sends response back to client
        return Response(serializer_instance.data)


# # APIView for deleting existing employee record
class EmployeeDelete(APIView):
    def delete(self,request,i):
        # reads record matching with id
        e=get_object_or_404(Employee,id=i)
        # deletes the record
        e.delete()
        # sends response back to client
        return Response({"message":"Deleted record Successfully"})

# # APIView for updating(fully) existing employee record
class EmployeeUpdate(APIView):
    def put(self,request,i):
        # reads the record matching with id
        e=get_object_or_404(Employee,id=i)
        # fetches the data coming from client
        data=request.data
        # calls Employee Serializer class for deserialization(validation+conversion)
        serializer_instance=EmployeeSerializer(instance=e,data=data)
        if serializer_instance.is_valid():
            # saves the record
            serializer_instance.save()
            # sends response back to client
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

# # APIView for updating(Partially)
class EmployeePartialUpdate(APIView):
    def patch(self,request,i):
        e=get_object_or_404(Employee,id=i)
        data=request.data
        serializer_instance=EmployeeSerializer(instance=e,data=data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)


