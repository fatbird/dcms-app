from django.contrib.auth.models import User
from django.views.generic import TemplateView

from rest_framework import viewsets

from core import models, serializers


class Home(TemplateView):
    template_name = 'home.html'


class About(TemplateView):
    template_name = 'about.html'


class Content(viewsets.ModelViewSet):

    queryset = models.Content.objects.all()
    serializer_class = serializers.Content


class LogEntries(viewsets.ModelViewSet):

    queryset = models.LogEntry.objects.all()
    serializer_class = serializers.LogEntry


class Images(viewsets.ModelViewSet):

    queryset = models.Image.objects.all()
    serializer_class = serializers.Image


class Users(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = serializers.User
