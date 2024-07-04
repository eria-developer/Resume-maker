from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserRegistrationSerializer, UserLoginSerializer, VerifyUserEmailSerializer, PasswordResetRequestSerializer, SetNewPasswordSerializer,LogoutSerializer
from rest_framework.response import Response
from rest_framework import status
from .utils import send_code_to_user
from .models import OneTimePassword
from rest_framework.permissions import IsAuthenticated
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import smart_str, DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .models import CustomUser


class RegisterUserView(GenericAPIView):
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        user_data = request.data 
        serializer = self.serializer_class(data=user_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = serializer.data  # corrected line
            send_code_to_user(user["email"])
            # send email function user["email"]
            return Response({
                "data": user,
                "message": f"hi {user['first_name']}, Your account has been created."
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class verifyUserEmail(GenericAPIView):
    serializer_class = VerifyUserEmailSerializer

    def post(self, request):
        otpcode = request.data.get("otp")
        try:
            user_code_object = OneTimePassword.objects.get(code=otpcode)
            user = user_code_object.user
            if not user.is_verified:
                user.is_verified = True
                user.save()
                return Response({
                    "message": "User email verified successfully"
                }, status=status.HTTP_200_OK)
            return Response({
                "message": "Otp code is invalid, user already verified"
            }, status=status.HTTP_204_NO_CONTENT)
        except OneTimePassword.DoesNotExist:
            return Response({
                "message": "passcode not provided"
            }, status=status.HTTP_404_NOT_FOUND)
        

class LoginUserView(GenericAPIView):
    serializer_class = UserLoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class TestAuthenticationView(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        data = {
            "message": "it works"
        }
        return Response(data, status=status.HTTP_200_OK)
    

class PasswordResetRequestView(GenericAPIView):
    serializer_class = PasswordResetRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        return Response({
            "message": "A link has been sent to your email to reset your password"
        }, status=status.HTTP_200_OK)
    

class PasswordResetConfirmView(GenericAPIView):
    def get(self, request, uidb64, token):
        try:
            user_id = smart_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=user_id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({
                    "message": f"Token is invalid or has expired"
                }, status=status.HTTP_401_UNAUTHORIZED)
            return Response({
                "success": True,
                "message": "Credentials are valid",
                "uidb64": uidb64,
                "token": token,
            }, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError:
            return Response({
                    "message": f"Token is invalid or has expired"
            }, status=status.HTTP_401_UNAUTHORIZED)
        

class SetNewPasswordView(GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({
                "message": "Your password has been reset"
            }, status=status.HTTP_200_OK)
        else:
            return Response({
               serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)
        

class LogoutUserView(GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)