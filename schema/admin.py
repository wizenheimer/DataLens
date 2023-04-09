from django.contrib import admin

# from accounts.models import SchemaEditorAssignment, SchemaViewerAssignment
from .models import Schema, Table, Column, DataSource, Dataset


# class editor_inline(admin.TabularInline):
#     model = SchemaEditorAssignment
#     extra = 1


# class viewer_inline(admin.TabularInline):
#     model = SchemaViewerAssignment
#     extra = 1


class SchemaAdmin(admin.ModelAdmin):
    model = Schema
    inlines = [
        # editor_inline,
        # viewer_inline,
    ]


admin.site.register(Schema, SchemaAdmin)
# admin.site.register(SchemaEditorAssignment)
# admin.site.register(SchemaViewerAssignment)
admin.site.register(DataSource)
admin.site.register(Dataset)
admin.site.register(Table)
admin.site.register(Column)
