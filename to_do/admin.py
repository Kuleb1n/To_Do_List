from django.contrib import admin

from .models import *

admin.site.site_header = 'To do list'
admin.site.site_title = 'To do list'


class RecordModelInline(admin.TabularInline):
    model = Record
    extra = 1


class ToDoListTitleAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')
    list_filter = ('title', 'user')
    list_select_related = ('user',)
    ordering = ('title',)
    inlines = [RecordModelInline]


class RecordAdmin(admin.ModelAdmin):
    list_display = ('record_title', 'status', 'title')
    list_filter = ('record_title', 'status', 'title')
    raw_id_fields = ('title',)
    ordering = ('title',)
    list_select_related = ('title',)


admin.site.register(ToDoListTitle, ToDoListTitleAdmin)
admin.site.register(Record, RecordAdmin)
