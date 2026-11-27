from django.db.models import Model
from django.shortcuts import render
from django.views import View

from app import serializers
from app.models import Student
from django.http import JsonResponse
from json import loads
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.views import Response
from app.serializers import StudentSerializer
from django.shortcuts import render,get_object_or_404

class StudentList(APIView):
    def get(self,request):
        #reads all students records from student table
        e=Student.objects.all()        #django format qs
        #converts the qs into python native using StudentSerializer
        serializer_instance=StudentSerializer(e,many=True)      #many-->more than one rows in table
        print(serializer_instance.data)
        return Response(serializer_instance.data)

class StudentCreate(APIView):                  # serializers used for conversion and validation
    def post(self,request):
        # data=request.data       #python native

        #validation+conversion(native to model object
        serializers_instance=StudentSerializer(data=request.data)
        print(request.data)
        #checks whether the data coming from client is valid,if valid saves the data into model
        if serializers_instance.is_valid():
            serializers_instance.save()             #save the data into model
            return Response(serializers_instance.data)      #sends created object as response

        #if data is not valid it shows the error
        else:
            return Response(serializers_instance.errors)


# # APIView for reading a specific student record
class StudentDetails(APIView):
    def get(self,request,i):
        # reads student record matching id
        # s=Student.objects.get(id=i)      #shows error if id is not in the table,to fix that given code is used(get_object_or_404)
        s=get_object_or_404(Student,id=i)
        # calls Student Serializer class for serialization
        serializer_instance=StudentSerializer(s)
        # sends response back to client
        return Response(serializer_instance.data)


# # APIView for deleting existing student record
class StudentDelete(APIView):
    def delete(self,request,i):
        # reads record matching with id
        s=get_object_or_404(Student,id=i)
        # deletes the record
        s.delete()
        # sends response back to client
        return Response({"message":"Deleted record Successfully"})

# # APIView for updating(fully) existing student record
class StudentUpdate(APIView):
    def put(self,request,i):
        # reads the record matching with id
        s=get_object_or_404(Student,id=i)
        # fetches the data coming from client
        data=request.data
        # calls Employee Serializer class for deserialization(validation+conversion)
        serializer_instance=StudentSerializer(instance=s,data=data)
        if serializer_instance.is_valid():
            # saves the record
            serializer_instance.save()
            # sends response back to client
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

# # APIView for updating(Partially)
class StudentPartialUpdate(APIView):
    def patch(self,request,i):
        s=get_object_or_404(Student,id=i)
        data=request.data
        serializer_instance=StudentSerializer(instance=s,data=data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

