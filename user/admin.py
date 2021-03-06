from django.contrib import admin
from .models import (
    Profile,
    UserFavourite,
    Requests,
    SeenRequest,
    Hire,
    RepairmanRequests,
    Appliccation,
    JobHire,
    ClientNotifications,
    RepairmanNotifications,
    Rate,
    RequestImages
)

# Register your models here.
admin.site.register(Profile)
admin.site.register(UserFavourite)
admin.site.register(Requests)
admin.site.register(SeenRequest)
admin.site.register(Hire)
admin.site.register(RepairmanRequests)
admin.site.register(Appliccation)
admin.site.register(JobHire)
admin.site.register(ClientNotifications)
admin.site.register(RepairmanNotifications)
admin.site.register(Rate)
admin.site.register(RequestImages)
