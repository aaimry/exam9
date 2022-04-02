from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from accounts.models import Profile

User = get_user_model()


class ProfileInline(admin.StackedInline):
    fields = ('photo', )
    model = Profile


class UserProfileAdmin(UserAdmin):
    inlines = (ProfileInline, )


admin.site.unregister(User)
admin.site.register(get_user_model(), UserProfileAdmin)
