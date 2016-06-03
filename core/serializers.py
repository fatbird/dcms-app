from django.contrib.auth.models import User as DjangoUser

from rest_framework import serializers

from dcms.serializers import Base64ImageField

from core.models import *


class Content(serializers.HyperlinkedModelSerializer):

    images = serializers.HyperlinkedRelatedField(many=True,
                                                 view_name='image-detail',
                                                 read_only=True)
    log_entries = serializers.HyperlinkedRelatedField(many=True,
                                                      view_name='logentry-detail',
                                                      read_only=True)

    class Meta:
        model = Content
        fields = ('uuid', 'title', 'body', 'images', 'created', 'start_date',
                  'end_date', 'log_entries', 'pk')


class LogEntry(serializers.ModelSerializer):

    content = serializers.HyperlinkedRelatedField(view_name='content-detail',
                                                  read_only=True)
    user = serializers.SlugRelatedField(read_only=True, slug_field='email')

    class Meta:
        model = LogEntry
        fields = ('content', 'user', 'when', 'action', 'pk', )


class Image(serializers.HyperlinkedModelSerializer):

    file = Base64ImageField()

    class Meta:
        model = Image
        fields = ('url', 'height', 'width', 'content', 'file', 'pk', )


class User(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = DjangoUser
        fields = ('email', 'first_name', 'last_name', 'url')
