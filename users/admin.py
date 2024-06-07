from django.contrib import admin
from django.contrib.auth.models import Group

from .models import *

admin.site.register(User)
admin.site.register(UserImage)
admin.site.register(Follow)
admin.site.unregister(Group)