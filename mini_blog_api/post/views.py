from django.shortcuts import render, get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from post.permissions import IsAuthorOrReadOnly
from post.serializers import PostSerializer
from rest_framework import status
from rest_framework.response import Response
from post.models import Post

# Create your views here.

class PostListCreate(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self,request):
        serializer_instance=PostSerializer(data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save(author=request.user)
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        p=Post.objects.filter()
        # p=Post.objects.filter(author=request.user)
        serializer_instance=PostSerializer(p,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)


class RetrieveUpdateDeletePost(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,IsAuthorOrReadOnly]

    def get(self,request,pk):
        p=get_object_or_404(Post,id=pk)
        self.check_object_permissions(request,p)
        serializer_instance=PostSerializer(p)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def put(self, request, pk):
        p=get_object_or_404(Post,id=pk)
        self.check_object_permissions(request,p)    # manually checks if requested user has permissions to perform the following operation
        serializer_instance=PostSerializer(instance=p,data=request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.data,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        p=get_object_or_404(Post,id=pk)
        self.check_object_permissions(request,p)
        p.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)