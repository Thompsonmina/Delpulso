from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.core.cache import cache

from rest_framework import generics, viewsets, mixins, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.decorators import action

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

# from .models import Post
# from .permissions import IsAuthorOrReadOnly
from .serializers import UserSerializer, EmailSerializer
from .throttle import MailJetLimitThrottle
from .models import Email


class CustomAuthToken(ObtainAuthToken):

	def post(self, request, *args, **kwargs):
		
		user = request.data.get('username')
		if user:
			user, _ = get_user_model().objects.get_or_create(username=user)

			token, created = Token.objects.get_or_create(user=user)
			return Response({
	            'token': token.key,
	            'user_id': user.pk,
	        })
		return Response({"username": "This field is required"}, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(viewsets.ModelViewSet):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer

	def get_permissions(self):
		if self.action == "create":
			permission_classes = [AllowAny]
		else:
			permission_classes = [IsAuthenticated]
		return [permission() for permission in permission_classes]

class listMail(generics.ListAPIView):
	serializer_class = EmailSerializer
	permission_classes = [IsAuthenticated]
	def get_queryset(self):
		return self.request.user.mails.all()

	def get_serializer_context(self):
		return {"save": True}


class sendMail(generics.CreateAPIView):
	queryset = Email.objects.all()
	serializer_class = EmailSerializer
	permission_classes = [IsAuthenticated] 
	throttle_classes = [MailJetLimitThrottle]

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)

		send_mail(serializer.validated_data["subject"], serializer.validated_data["message"],
			"noreply@flamboyant.email",
			[serializer.validated_data["recepient"]])

		if serializer.validated_data.get("save"):
			return super().create(request)

		return Response({"message": "email sent"}, status=status.HTTP_200_OK)

	
	def perform_create(self, serializer):
		return serializer.save(sender=self.request.user)
