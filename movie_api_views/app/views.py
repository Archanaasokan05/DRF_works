

from rest_framework import mixins,generics,viewsets

from app.models import Movie
from app.serializers import MovieSerializer

# # ----------Mixins----------

# # APIView for listing and creating movie record
# class MovieListCreate(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
# # APIView for read/update/delete existing movie record
# class MovieRetrieveUpdateDelete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#
#     def put(self,request,pk):
#         return self.update(request,pk)
#
#     def patch(self,request,pk):
#         return self.partial_update(request,pk)
#
#     def delete(self,request,pk):
#         return self.destroy(request,pk)


# # -----------Generics----------
#
# class MovieListCreate(generics.ListAPIView,generics.CreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
# class MovieRetrieveUpdateDelete(generics.RetrieveAPIView,generics.UpdateAPIView,generics.DestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


# ----------Viewsets----------

class  MovieView(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
