from django.contrib import admin
from .models import Profile, UserFavourite, Requests, SeenRequest

# Register your models here.
admin.site.register(Profile)
admin.site.register(UserFavourite)
admin.site.register(Requests)
admin.site.register(SeenRequest)
