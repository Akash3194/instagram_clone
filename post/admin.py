from django.contrib import admin
from .models import Post, MediaFile

# Register your models here.
admin.site.register([Post, MediaFile])
