from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Comment
from .serializers import (
    RegistrationSerializer,
    UserSerializer,
    LoginSerializer,
    UserProfileSerializer,
    CommentSerializer,
    UpdateCommentSerializer
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

    @action(detail=False, methods=['PUT', 'PATCH', 'GET', 'DELETE'])
    def me(self, request):

        if request.method in ('PUT', 'PATCH'):
            instance = request.user
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(serializer.data)

        elif request.method == 'GET':
            instance = request.user
            serializer = self.get_serializer(instance)

            return Response(serializer.data)

        elif request.method == 'DELETE':
            instance = request.user
            instance.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        if self.action == 'me':
            return UserSerializer
        return self.serializer_class


class CommentViewSet(
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    #filtros de usuario y de camiseta

    def create(self, request, *args, **kwargs):
        request.data['user'] = request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.action in ("update", "partial_update"):
            return UpdateCommentSerializer
        return self.serializer_class