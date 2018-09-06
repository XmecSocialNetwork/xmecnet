from django.contrib import admin
from .models import Profile, Email, WorkExperience, Telegram, Education

# Register your models here.

admin.site.register(Profile)
admin.site.register(WorkExperience)
admin.site.register(Telegram)
admin.site.register(Email)
admin.site.register(Education)
