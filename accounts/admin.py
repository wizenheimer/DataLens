from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User, TeamAssignment, SnippetAssignment, SchemaAssignment


class team_inline(admin.TabularInline):
    model = TeamAssignment
    extra = 1


class snippet_inline(admin.TabularInline):
    model = SnippetAssignment
    extra = 1


class schema_inline(admin.TabularInline):
    model = SchemaAssignment
    extra = 1


class UserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    inlines = [
        team_inline,
        snippet_inline,
        schema_inline,
    ]
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "email",
        "is_staff",
        "is_active",
    )
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "password",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(User, UserAdmin)
admin.site.register(TeamAssignment)
admin.site.register(SnippetAssignment)
admin.site.register(SchemaAssignment)
