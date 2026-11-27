from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from task.models import Task
from task.permissions import IsOwner
from task.serializers import TaskSerializer

# Create your views here.

# class TaskListCreate(APIView):
#     permission_classes = [IsAuthenticated]
#     authentication_classes = [TokenAuthentication]
#
#     def get(self,request):
#         # Task list of particular user
#         t=Task.objects.filter(user=request.user)
#         serializer_instance=TaskSerializer(t,many=True)
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)
#
#     def post(self,request):
#         serializer_instance=TaskSerializer(data=request.data)   #title,description,completed
#         if serializer_instance.is_valid():
#             serializer_instance.save(user=request.user)
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)



# -----------------------using generics-----------------------


from rest_framework import generics
class TaskListCreate(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    # To add custom logic inside generics view we override get_queryset()
    # and perform_create()
    # for creation -> perform_create()
    # for list -> get_queryset()
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)






class RetrieveUpdateDelete(APIView):
    permission_classes = [IsAuthenticated,IsOwner]
    authentication_classes = [TokenAuthentication]

    def get(self,request,pk):
        t=get_object_or_404(Task,id=pk)
        # self.check_object_permissions(request,t)
        serializer_instance=TaskSerializer(t)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def put(self,request,pk):
        t=get_object_or_404(Task,id=pk)
        # self.check_object_permissions(request,t)
        serializer_instance=TaskSerializer(instance=t,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(user=request.user)
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.data,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        t=get_object_or_404(Task,id=pk)
        # self.check_object_permissions(request,t)
        t.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

