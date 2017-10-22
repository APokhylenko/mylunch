from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from import_export import resources
from import_export.admin import ImportMixin

from .models import User


class UserResource(resources.ModelResource):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email')
        import_id_fields = ['email']


class UserAdminn(ImportMixin, UserAdmin):
    resource_class = UserResource

admin.site.register(User, UserAdminn)
