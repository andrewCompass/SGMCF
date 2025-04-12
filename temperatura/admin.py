from django.contrib import admin

from temperatura.models import Logs


# Register your models here.

@admin.register(Logs)
class LogsAdmin(admin.ModelAdmin):
    list_display = ('temperatura', 'status', 'data')
    search_fields = ('temperatura', 'status', 'data')
    ordering = ('-data',)
    list_per_page = 10
    empty_value_display = '- vazio -'

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False