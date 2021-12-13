
from django.contrib import admin
from django.urls import path, include, re_path
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth", include("rest_framework.urls")),
    re_path('', include('mails.urls')),
    re_path("^/?$", lambda req: HttpResponse("Ok!")),

]
