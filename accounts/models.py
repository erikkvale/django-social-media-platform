from django.db import models
from django.contrib import auth


class User(auth.models.User, auth.models.PermissionMixin):
    def __str__(self):
        return "@{}".format(self.username)