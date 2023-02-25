from rest_framework.views import APIView, Request, Response, status
from .models import User
from .serializer import UserSerializer, LoginSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdmOrUserToUser
from rest_framework.pagination import PageNumberPagination


class LoginView(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)

        if not user:
            return Response({"detail": "No active account found with the given credentials"}, status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return_dict = {
  "refresh": str(refresh),
  "access": str(refresh.access_token)
}

        return Response(return_dict, status.HTTP_200_OK)
        



class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.validated_data["is_employee"] == True:
            serializer.validated_data["is_superuser"] = True

        if User.objects.filter(email=serializer.validated_data["email"]).exists():
            return Response({}, status.HTTP_201_CREATED)

        user = User.objects.create_user(**serializer.validated_data)

        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_201_CREATED)

class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmOrUserToUser]

    def get(self, request: Request, user_id) -> Response:
        user = get_object_or_404(User, pk=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)
    
    def patch(self, request: Request, user_id) -> Response:
        user = get_object_or_404(User, pk=user_id)
        self.check_object_permissions(request, user)

    
        serializer = UserSerializer(user, request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status.HTTP_200_OK)
