from django.contrib import admin
from .models import Snippet
from accounts.models import EditorAssignment, ViewerAssignment


class editor_inline(admin.TabularInline):
    model = EditorAssignment
    extra = 1


class viewer_inline(admin.TabularInline):
    model = ViewerAssignment
    extra = 1


class SnippetAdmin(admin.ModelAdmin):
    model = Snippet
    inlines = [
        editor_inline,
        viewer_inline,
    ]


admin.site.register(Snippet, SnippetAdmin)
admin.site.register(EditorAssignment)
admin.site.register(ViewerAssignment)
