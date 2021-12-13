from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views

from .views import UserViewSet, CustomAuthToken, sendMail, listMail


router = SimpleRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls

urlpatterns += [
    path('user-token/', CustomAuthToken.as_view()),
    path("email/send", sendMail.as_view()),
    path("email/emails", listMail.as_view())
]