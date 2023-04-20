from django.contrib import admin
from .models import Record


class RecordAdmin(admin.ModelAdmin):
    list_display = ["user", "question", "language", "created_on"]
    list_filter = ["language"]
    search_fields = ["language"]


admin.site.register(Record, RecordAdmin)
