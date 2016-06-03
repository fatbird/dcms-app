import logging
from uuid import uuid4

from django.db import models
from django.contrib.auth.models import User

log = logging.getLogger('django.request')


class Content(models.Model):
    """A basic content piece"""

    uuid = models.UUIDField(primary_key=True, default=uuid4)
    title = models.TextField(blank=True)
    body = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Content'

    def save(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        exists = self.pk is not None
        super(Content, self).save(*args, **kwargs)
        if user is not None:
            if exists:
                action = LogEntry.ACTIONS[1]
            else:
                action = LogEntry.ACTIONS[0]
            LogEntry.objects.create(content=self, user=user, action=action)

    def __unicode__(self):
        if self.title.strip() == '':
            return self.uuid
        return self.title


class LogEntry(models.Model):
    """An action on the Content item"""

    ACTIONS = (
        ('add', 'Created'),
        ('edit', 'Modified'),
        ('delete', 'Deleted'),
    )

    content = models.ForeignKey(Content, related_name='log_entries')
    user = models.ForeignKey(User, related_name='content_logs')
    when = models.DateTimeField(auto_now_add=True)
    action = models.TextField(choices=ACTIONS, default=ACTIONS[0][0])
    diff = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Log Entry'
        verbose_name_plural = 'Log Entries'


def file_name(instance, filename):
    return '%s.%s' % (instance.uuid.hex, filename.split('.')[-1])


class Image(models.Model):
    """An image that may be associated with a Content item"""

    uuid = models.UUIDField(primary_key=True, default=uuid4)
    content = models.ManyToManyField(Content, related_name='images',
                                     blank=True)
    file = models.ImageField(height_field='height', width_field='width',
                             upload_to=file_name, blank=True)
    height = models.PositiveIntegerField(blank=True, null=True)
    width = models.PositiveIntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """Delete an existing file on updating file, then save as usual"""
        try:
            this = Image.objects.get(pk=self.pk)
            if this.file != self.file:
                this.file.delete()
        except Image.DoesNotExist: pass
        super(Image, self).save(*args, **kwargs)



