from django.contrib import admin
from .models import*

# Register your models here.

admin.site.register(ContactForm)
# admin.site.register(Services)
admin.site.register(Service_detail)

class Services_admin(admin.ModelAdmin):
    list_display = ("title", "image")

admin.site.register(Services,Services_admin)