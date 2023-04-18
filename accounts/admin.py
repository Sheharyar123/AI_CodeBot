from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# For language translations
from django.utils.translation import gettext_lazy as _

User = get_user_model()


# Change Admin titles
admin.site.site_header = "OpenAI Codebot Admin"
admin.site.site_title = "OpenAI Codebot Admin"
admin.site.index_title = "OpenAI Codebot Administration"


class UserAdmin(BaseUserAdmin):
    list_display = ["email", "name", "is_active", "is_superuser"]
    search_fields = ["name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal Details"), {"fields": ("name",)}),
        (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser")}),
        (_("Important Dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        None,
        {
            "classes": ("wide",),
            "fields": (
                "name",
                "email",
                "password",
                "is_active",
                "is_staff",
                "is_superuser",
            ),
        },
    )
    readonly_fields = ["last_login"]
    ordering = ["id"]


admin.site.register(User, UserAdmin)
