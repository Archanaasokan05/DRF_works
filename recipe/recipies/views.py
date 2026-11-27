from django.db.models import Model
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from recipies.models import Recipie
from recipies.serializers import RecipieSerializer

# Create your views here.

class RecipieCreateList(APIView):
    # view all recipies
    def get(self,request):
        r=Recipie.objects.all()
        serializer_instance=RecipieSerializer(r,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    # create a new recipie
    def post(self,request):
        serializer_instance=RecipieSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class RetrieveUpdateDelete(APIView):

    # read a specific recipie
    def get(self,request,pk):
        r=get_object_or_404(Recipie,id=pk)
        serializer_instance=RecipieSerializer(r)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    # update an existing recipie
    def put(self,request,pk):
        r=get_object_or_404(Recipie,id=pk)
        serializer_instance=RecipieSerializer(instance=r,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.data,status=status.HTTP_400_BAD_REQUEST)

    # delete recipie
    def delete(self,request,pk):
        r=get_object_or_404(Recipie,id=pk)
        r.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Search APIView
from django.db.models import Q
class SearchAPIView(APIView):

    def get(self, request):

        # Fetch keyword from query parameters
        data = request.query_params.get('search')

        # Search recipes using multiple fields
        r = Recipie.objects.filter(
            Q(recipie_name__icontains=data) |
            Q(ingredients__icontains=data)
            # Q(instructions__icontains=data) |
            # Q(mealtype__icontains=data) |
            # Q(cusine__icontains=data)
        )

        # Call serializer for serialization
        serializer_instance = RecipieSerializer(r, many=True)

        # Return response to client
        return Response(serializer_instance.data)