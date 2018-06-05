from django.db import models
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from groups.models import Group
import misaka


User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name='posts')
    created_at = models.DateTimeField(auto_now=True)
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name='posts', null=True, blank=True)

    def __str__(self):
        return self.message

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.message_html = misaka.html(self.message)
        super().save()

    def get_absolute_url(self):
        return reverse(
            viewname='posts:single',
            kwargs={
                'username': self.user.username,
                'pk': self.pk,
            }
        )

    class Meta:
        ordering = (
            '-created_at'
        )
        unique_together = (
            'user',
            'message',
        )