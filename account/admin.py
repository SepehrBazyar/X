from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User as BaseUser

from account.models import User

# Register your models here.
# admin.site.unregister(BaseUser)

@admin.register(User)
class NewUserAdmin(UserAdmin):
    list_display = (
        "id",
        "phone_number",
        "email",
    )
