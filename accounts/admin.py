from django.contrib import admin
from accounts.models import Profile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class ProfileInline(admin.StackedInline):
    """
    Defines inline admin options for the Profile model.
    """
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class ExtendedUserAdmin(BaseUserAdmin):
    """
    Extends the BaseUserAdmin class to include inline editing of profiles.
    """
    inlines = (ProfileInline,)

    def get_inline_instances(self, request, obj=None):
        """
        Overrides the get_inline_instances method to conditionally display the inline based on whether an object is being edited.
        """
        if not obj:
            return list()
        return super(ExtendedUserAdmin, self).get_inline_instances(request, obj)


""" Unregister the default User model admin to replace it with the ExtendedUserAdmin """
admin.site.unregister(User)

""" Register the User model with the ExtendedUserAdmin to include profile inline """
admin.site.register(User, ExtendedUserAdmin)

""" Register the Profile model directly with the admin site to manage profiles separately """
admin.site.register(Profile)
