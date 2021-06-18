from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from Account.serializers import AuthenticationSerializer, UserSerializer, PasswordChangeSerializer
from rest_framework.authtoken.views import Token

User = get_user_model()


class AuthApi(GenericAPIView):
    serializer_class = AuthenticationSerializer
    authentication_classes = [TokenAuthentication]

    def post(self, request, *args, **kwargs):
        # Serialize Data
        serialized_data = self.get_serializer(data=self.request.data)
        if serialized_data.is_valid():
            # Get User
            user = serialized_data.validated_data["user"]
            # Create Auth Token
            token, created = Token.objects.get_or_create(user=user)
            # Return Response
            return Response({
                "user": UserSerializer(instance=user).data,
                "token": token.key
            })
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        # IF USER IS Authenticated
        if request.user.is_authenticated:
            # Create Auth Token
            token, created = Token.objects.get_or_create(user=request.user)
            # Return Response
            return Response({
                "user": UserSerializer(instance=request.user).data,
                "token": token.key
            })
        return Response({"error": ["Unauthorized User"]}, status=status.HTTP_401_UNAUTHORIZED)


class ChangePasswordApi(GenericAPIView):
    serializer_class = PasswordChangeSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serialized_data = self.get_serializer(data=request.data)

        if serialized_data.is_valid():
            user = serialized_data.save()
            token, created = Token.objects.get_or_create(user=user)
            token.delete()
            new_token = Token.objects.create(user=user)
            return Response({
                "token": new_token.key
            }, status=status.HTTP_201_CREATED)
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountUpdateApi(GenericAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.get_queryset()
    lookup_field = "id"
    model = User
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        data = self.get_serializer(instance=request.user, data=request.data, partial=True)
        if data.is_valid():
            user = data.save()
            return Response(data.data, status=status.HTTP_200_OK)

        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)