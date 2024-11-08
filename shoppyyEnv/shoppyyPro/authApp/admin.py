from django.contrib import admin
from .models import Registeruser


# class UserAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'is_active')

# # Register your models here.
# admin.site.register(Registeruser, UserAdmin)
admin.site.register(Registeruser)
