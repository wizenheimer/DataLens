from django.contrib import admin
from .models import Schema, Table, Column

from django.contrib import admin
from .models import Schema
from accounts.models import SchemaEditorAssignment, SchemaViewerAssignment


class editor_inline(admin.TabularInline):
    model = SchemaEditorAssignment
    extra = 1


class viewer_inline(admin.TabularInline):
    model = SchemaViewerAssignment
    extra = 1


class SchemaAdmin(admin.ModelAdmin):
    model = Schema
    inlines = [
        editor_inline,
        viewer_inline,
    ]


admin.site.register(Schema, SchemaAdmin)
admin.site.register(SchemaEditorAssignment)
admin.site.register(SchemaViewerAssignment)
# admin.site.register(Schema)
admin.site.register(Table)
admin.site.register(Column)
