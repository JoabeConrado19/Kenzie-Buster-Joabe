from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from .models import Movie, MovieOrder
from users.models import User
from .serializer import MovieSerializer, MovieOrderSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.shortcuts import get_object_or_404
from .permissions import IsAdminOrReadOnly
from rest_framework.pagination import PageNumberPagination



# Create your views here.


class MovieView(APIView, PageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request) -> Response:
        movies = Movie.objects.all()
        result_page = self.paginate_queryset(movies, request)
        serializer = MovieSerializer(result_page, many=True)


        return self.get_paginated_response(serializer.data)
    

    def post(self, request: Request) -> Response:
        request.data["added_by"] = request.user.email

        serializer = MovieSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
       
        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)


class MovieDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUser]


    def delete(self, request: Request, movie_id:int) -> Response:
        movie = get_object_or_404(Movie, pk=movie_id)
        movie.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request: Request) -> Response:
        movies = MovieOrder.objects.all()
        serializer = MovieOrderSerializer(movies, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
    

    def post(self, request: Request, movie_id:int) -> Response:
        request.data["buyed_by"] = request.user.email
        movie = get_object_or_404(Movie, pk=movie_id)
        request.data["title"] = movie.title

        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
       
        serializer.save(movie=movie, user=request.user)

        return Response(serializer.data, status.HTTP_201_CREATED)


    