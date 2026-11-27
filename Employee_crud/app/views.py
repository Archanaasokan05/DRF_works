from django.shortcuts import render, get_object_or_404
from app.models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers import EmployeeSerializer
from django.db.models import Q

# # APIView for reading all records
# class EmployeeList(APIView):
#     def get(self,request):
#         #reads all employee records from Employee table
#         e=Employee.objects.all()        #django format qs
#         #converts the qs into python native using EmployeeSerializer
#         serializer_instance=EmployeeSerializer(e,many=True)
#         print(serializer_instance.data)
#         return Response(serializer_instance.data)
#
#
# # # APIView for creating a new record
# class EmployeeCreate(APIView):                  # serializers used for conversion and validation
#     def post(self,request):
#         # data=request.data       #python native
#
#         #validation+conversion(native to model object
#         serializers_instance=EmployeeSerializer(data=request.data)
#         print(request.data)
#
#         #checks whether the data coming from client is valid,if valid saves the data into model
#         if serializers_instance.is_valid():
#             serializers_instance.save()             #save the data into model
#             return Response(serializers_instance.data)      #sends created object as response
#
#         #if data is not valid it shows the error
#         else:
#             return Response(serializers_instance.errors)
#
#
# # # APIView for reading a specific employee record
# class EmployeeDetail(APIView):
#     def get(self,request,i):
#         # reads employee record matching id
#         # e=Employee.objects.get(id=i)      #shows error if id is not in the table,to fix that given code is used(get_object_or_404)
#         e=get_object_or_404(Employee,id=i)
#         # calls Employee Serializer class for serialization
#         serializer_instance=EmployeeSerializer(e)
#         # sends response back to client
#         return Response(serializer_instance.data)
#
#
# # # APIView for deleting existing employee record
# class EmployeeDelete(APIView):
#     def delete(self,request,i):
#         # reads record matching with id
#         e=get_object_or_404(Employee,id=i)
#         # deletes the record
#         e.delete()
#         # sends response back to client
#         return Response({"message":"Deleted record Successfully"})
#
# # # APIView for updating(fully) existing employee record
# class EmployeeUpdate(APIView):
#     def put(self,request,i):
#         # reads the record matching with id
#         e=get_object_or_404(Employee,id=i)
#         # fetches the data coming from client
#         data=request.data
#         # calls Employee Serializer class for deserialization(validation+conversion)
#         serializer_instance=EmployeeSerializer(instance=e,data=data)
#         if serializer_instance.is_valid():
#             # saves the record
#             serializer_instance.save()
#             # sends response back to client
#             return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)
#
# # # APIView for updating(Partially)
# class EmployeePartialUpdate(APIView):
#     def patch(self,request,i):
#         e=get_object_or_404(Employee,id=i)
#         data=request.data
#         serializer_instance=EmployeeSerializer(instance=e,data=data,partial=True)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)
#
#


# ================================================================================================

# Using Mixin class-------
from rest_framework import mixins, generics, viewsets


# class EmployeeList(mixins.ListModelMixin,generics.GenericAPIView):
#     queryset=Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     def get(self,request):
#         return self.list(request)
#
# class EmployeeDetail(mixins.RetrieveModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     def get(self,request,pk):
#         return self.retrieve(request)
#
# class EmployeeCreate(mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     def post(self,request):
#         return self.create(request)
#
# class EmployeeUpdate(mixins.UpdateModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     def put(self,request,pk):
#         return self.update(request)
#
# class EmployeePartialUpdate(mixins.UpdateModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     def patch(self,request,pk):
#         return self.partial_update(request)
#
# class EmployeeDelete(mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     def delete(self,request,pk):
#         return self.destroy(request)


# Using Generics-------

# class EmployeeList(generics.ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# class EmployeeCreate(generics.CreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# class EmployeeDetail(generics.RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# class EmployeeUpdate(generics.UpdateAPIView):
#     # PUT/PATCH                           # we can update fully and partially in one class while  using generics
#                                           # if we use one class,we need to use one path for put/patch in url also
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
# class EmployeeDelete(generics.DestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# Using Viewsets---------

class EmployeeView(viewsets.ModelViewSet): #GET/POST/PUT/PATCH/DELETE
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class SearchAPIView(APIView):
    def get(self,request):
        data=request.query_params.get('search')
        print(data)
        e=Employee.objects.filter(Q(Name__icontains=data)|
                                  Q(Empid__icontains=data)|
                                  Q(Age__icontains=data)|
                                  Q(Place__icontains=data)|
                                  Q(Gender__icontains=data)|
                                  Q(Salary__icontains=data)|
                                  Q(Designation__icontains=data))

        serializer_instance=EmployeeSerializer(e,many=True)
        return Response(serializer_instance.data)

# Register
from rest_framework import status
from app.serializers import UserSerializer

class RegisterView(APIView):
    def post(self,request):
        serializer_instance=UserSerializer(data=request.data)  #deserialization [conversion + validation]
        if serializer_instance.is_valid():

            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
