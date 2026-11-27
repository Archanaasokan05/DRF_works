from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from app.models import Book,BookIssue
from app.serializers import BookSerializer, BookIssueSerializer


# Create your views here.


class BookListCreate(APIView):
    def post(self,request):
        serializer_instance=BookSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        qs=Book.objects.all()
        serializer_instance=BookSerializer(qs,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

class BookIssueListCreate(APIView):
    def post(self,request):
        serializer_instance=BookIssueSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        b=BookIssue.objects.all()
        serializer_instance=BookIssueSerializer(b,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

class BookIssueDelete(APIView):
    def delete(self,request,pk):
        b=get_object_or_404(BookIssue,id=pk)
        b.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
