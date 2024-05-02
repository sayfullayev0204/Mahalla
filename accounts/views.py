from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.core.exceptions import PermissionDenied
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from django.contrib.auth import get_user_model
from .serializers import UserSerializer


User = get_user_model()


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(request, username=username, password=password)
        if user is None:
            raise AuthenticationFailed("Invalid credentials")

        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        refresh_token = str(refresh)

        serializer = UserSerializer(user)
        user_data = serializer.data

        return Response(
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
                "user": user_data,
            }
        )


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh_token")
            if not refresh_token:
                return Response(
                    {"error": "Refresh token is required."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {"success": "User logged out successfully."}, status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        role = serializer.validated_data["role"]
        rank = self.get_rank_for_role(role)

        new_user = User(
            username=serializer.validated_data["username"],
            first_name=serializer.validated_data["first_name"],
            last_name=serializer.validated_data["last_name"],
            role=role,
            rank=rank,
        )

        if not self.can_create_user_with_rank(request.user, rank):
            raise PermissionDenied(
                "You don't have permission to create a user with this role."
            )

        new_user.set_password(serializer.validated_data["password"])
        new_user.save()

        headers = self.get_success_headers(serializer.data)
        return Response(
            self.serializer_class(new_user).data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        else:
            return User.objects.filter(rank__lte=self.request.user.rank)

    def get_rank_for_role(self, role):
        if role == User.ROLE_ADMIN:
            return 4
        elif role in [User.ROLE_HOKIM, User.ROLE_HOKIM_YORDAMCHISI]:
            return 3
        elif role in [User.ROLE_TUMAN_MASUL, User.ROLE_TUMAN_YOSHLAR_ISHLARI]:
            return 2
        elif role in [User.ROLE_MAHALLA_MASUL, User.ROLE_MAKTAB_MASUL]:
            return 1
        else:
            raise ValueError(f"Unknown role: {role}")

    def can_create_user_with_rank(self, user, requested_rank):
        if user.is_superuser:
            return True

        if user.rank > requested_rank:
            return True

        return False


# class UserViewSet(ModelViewSet):
#     serializer_class = UserSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated, CanCreateLowerRankUser]

#     def get_queryset(self):
#         if self.request.user.is_superuser:
#             return User.objects.all()
#         else:
#             return User.objects.filter(rank__lte=self.request.user.rank)

#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         role = serializer.validated_data["role"]
#         if role == User.ROLE_ADMIN:
#             rank = 4
#         elif role in [User.ROLE_HOKIM, User.ROLE_HOKIM_YORDAMCHISI]:
#             rank = 3
#         elif role in [User.ROLE_TUMAN_MASUL, User.ROLE_TUMAN_YOSHLAR_ISHLARI]:
#             rank = 2
#         elif role in [User.ROLE_MAHALLA_MASUL, User.ROLE_MAKTAB_MASUL]:
#             rank = 1
#         else:
#             raise ValueError(f"Unknown role: {role}")

#         new_user = User(
#             username=serializer.validated_data["username"],
#             first_name=serializer.validated_data["first_name"],
#             last_name=serializer.validated_data["last_name"],
#             role=role,
#             rank=rank,
#         )
#         print(new_user.rank)

#         if not self.check_permissions(request):
#             raise PermissionDenied(
#                 "You don't have permission to create a user with this role."
#             )

#         new_user.set_password(serializer.validated_data["password"])
#         new_user.save()

#         headers = self.get_success_headers(serializer.data)
#         return Response(
#             self.serializer_class(new_user).data,
#             status=status.HTTP_201_CREATED,
#             headers=headers,
#         )
