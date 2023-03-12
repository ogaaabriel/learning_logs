from django.contrib import admin

from . import models


@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ["title", "public", "date_created", "owner"]
    search_fields = ["title"]
    list_filter = ["public", "date_created", "owner"]


@admin.register(models.Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ["content", "date_created", "topic"]
    list_filter = ["date_created", "topic"]
