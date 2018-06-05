from django.contrib import admin
from . import models

# Allows parent-child model view and edit on same page
class GroupMemberInLine(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
