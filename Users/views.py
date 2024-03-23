
from django.core.mail import send_mail, mail_admins, BadHeaderError, EmailMessage
from django.shortcuts import render
from templated_mail.mail import BaseEmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework import status

from .models import CustomUser
from .serializers import CustomUserSerializer


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class IsAuthenticatedView(APIView):
    def get(self, request):
        # Your view logic here
        return Response({"message": "Authenticated successfully"})


@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class GetCurrentUserView(APIView):
    def get(self, request):
        serializer = CustomUserSerializer(
            request.user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    # only admins
    permission_classes = [AllowAny]

# create user and send mail


class RegistrationAPIView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            send_email(request)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def send_email(request):
    try:
        message = BaseEmailMessage(
            to=['bedynek.timon@gmail.com'],
            template_name='emails/registrationlink.html',
            context={
                'subject': 'Gaming Backend Email Verification Link',
                'testuser': request.data['username'],
                'link': 'https://gaming-frontend-one.vercel.app',

            }
        )
        message.send(to=[request.data['email']])

    except BadHeaderError:
        pass
    return render(request, 'emails/registrationlink.html', {'message': 'Email sent successfully'})
