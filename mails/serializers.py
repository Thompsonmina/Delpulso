from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Email

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = ["id", "username"]


class EmailSerializer(serializers.ModelSerializer):
	save = serializers.BooleanField(default=False)
	sender = serializers.PrimaryKeyRelatedField(read_only=True)

	class Meta:
		model = Email
		fields = "__all__" 

	def create(self, validated_data):
		validated_data.pop("save")
		return super().create(validated_data)
  	
	