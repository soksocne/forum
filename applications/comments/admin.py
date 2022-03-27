from django.contrib import admin

# Register your models here.
from applications.comments.models import Comments

admin.site.register(Comments)
