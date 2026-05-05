from django.contrib import admin
from . import models


class RecordTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


class RecordAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'phone', 'preferred_timing', 'record_type', 'created_at']
    list_filter = ['record_type__title']
    search_fields = ['text', 'phone']


class MessagesAdmin(admin.ModelAdmin):
    list_display = ['theme', 'message', 'attachment']
    search_fields = ['theme', 'message']


admin.site.register(models.Messages, MessagesAdmin)
admin.site.register(models.RecordType, RecordTypeAdmin)
admin.site.register(models.Record, RecordAdmin)