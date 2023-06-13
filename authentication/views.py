from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import (
    RegistrationSerializer,
    UserSerializer,
    LoginSerializer,
    UserProfileSerializer
)
from rest_framework.viewsets import mixins, GenericViewSet


class RegisterViewSet(mixins.CreateModelMixin, GenericViewSet):
    permission_classes = [AllowAny]
    serializer_class = RegistrationSerializer


class UserLoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request): #Login
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "first_name"

    @action(detail=True, methods=['PUT', 'PATCH', 'DELETE'])
    def me(self, request):

        if request.method in ('PUT', 'PATCH'):
            instance = selg.get_object
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)

        elif request.method == "GET":

            instance = selg.get_object
            serializer = self.get_serializer(instance)
            return Response(serializer.data)

    def get_serializer_class(self):
        if self.action == "me":
            return self.serializer_class
        return UserSerializer
