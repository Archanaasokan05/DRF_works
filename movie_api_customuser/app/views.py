from email.policy import HTTP

from django.db.migrations import serializer
from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from app.serializers import MovieSerializer
from app.models import Movie
from django.shortcuts import render,get_object_or_404
from rest_framework import status
from django.db.models import Q

# APIView for creating a new movie record
class MovieCreate(APIView):
    def post(self,request):
        serializer_instance=MovieSerializer(data=request.data)  #deserialization [conversion + validation]
        if serializer_instance.is_valid():
            # -----------------
            print(serializer_instance.validated_data)
            director=serializer_instance.validated_data['director']
            print(director)
            # -----------------
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

#  APIView for reading all movie records
class MovieList(APIView):
    def get(self,request):
        m=Movie.objects.all()
        serializer_instance=MovieSerializer(m,many=True)
        print(serializer_instance.data)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

# APIView for reading a specific movie record
class MovieDetails(APIView):
    def get(self,request,i):
        m=get_object_or_404(Movie,id=i)
        serializer_instance=MovieSerializer(m)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

# APIView for updating a particular record
class MovieUpdate(APIView):
    def put(self,request,i):
        m=get_object_or_404(Movie,id=i)
        serializer_instance=MovieSerializer(instance=m,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


# APIView for updating(partialy) a particular record
class MoviePartialUpdate(APIView):
    def patch(self,request,i):
        m=get_object_or_404(Movie,id=i)
        serializer_instance=MovieSerializer(instance=m,data=request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

#APIView for deleting a movie record
class MovieDelete(APIView):
    def delete(self,request,i):
        m=get_object_or_404(Movie,id=i)
        m.delete()
        # return Response({"message":"Deleted Record Successfully"})
        return Response({"message": "Deleted"}, status=status.HTTP_204_NO_CONTENT)

# Search APIView
# class SearchAPIView(APIView):
#     def get(self,request):
#         # fetches the keyword from query parameters
#         data=request.query_params.get('search')
#         print(data)
#
#         # Reads all records matching with keyword from db table(using filter)
#         m=Movie.objects.filter(Q(title__icontains=data) |
#                                 Q(director__icontains=data) |
#                                 Q(language__icontains=data) |
#                                 Q(year__icontains=data))
#
#         # filter  -->more than one matching keywords
#         # field lookups   -->field comparison
#         # Q object   --> while using or(|),and in ORM query
#
#         # Call Serializer class for Serialization
#         serializer_instance=MovieSerializer(m,many=True)
#
#         # return Response back to client
#         return Response(serializer_instance.data)

# --------------------------------------------

from rest_framework.filters import SearchFilter
from rest_framework import generics

class SearchAPIView(generics.ListAPIView):
    queryset=Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter]
    search_fields=['title','director','language','year']

from app.serializers import UserSerializer

class RegisterView(APIView):
    def post(self,request):
        serializer_instance=UserSerializer(data=request.data)  #deserialization [conversion + validation]
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class RegisterAPIView(APIView):
    def post(self,request):
        serializer_instance=UserSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_instance.errors, status=status.HTTP_400_BAD_REQUEST)