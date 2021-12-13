from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Email(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
         on_delete=models.CASCADE, related_name="mails"
    )
    message = models.TextField()
    subject = models.TextField()
    recepient = models.EmailField()
    anon = models.BooleanField(default=False)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

