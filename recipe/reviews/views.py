from django.shortcuts import render
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status
from reviews.serializers import ReviewSerializer
from rest_framework.response import Response

# Create your views here.

class CreateReview(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        print(request.user)
        u=request.user  #current user object
        serializer_instance=ReviewSerializer(data=request.data) #recipe,comment,rating
        if serializer_instance.is_valid():
            serializer_instance.save(user=u)
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

from reviews.models import Review
from django.shortcuts import get_object_or_404

class ReadReview(APIView):
    def get(self,request,pk):   #recipe id
        qs=Review.objects.filter(recipe=pk) #read all reviews matching recipe id pk
        serializer_instance=ReviewSerializer(qs,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

# update an existing review
from reviews.permissions import IsOwner
class UpdateReview(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated,IsOwner]
    def put(self, request, pk):
        r = get_object_or_404(Review, id=pk)

        self.check_object_permissions(request,r)    # manually checks if requested user has permissions to perform the following operation
        serializer_instance = ReviewSerializer(instance=r, data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.data, status=status.HTTP_400_BAD_REQUEST)

        # delete review

    def delete(self, request, pk):
        r = get_object_or_404(Review, id=pk)
        r.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

