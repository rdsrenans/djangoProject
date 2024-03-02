from django.contrib import admin
from core.models import Eventos


# Register your models here.
class EventosAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'data_evento', 'data_criacao')
    list_filter = ('titulo', 'data_evento',)


admin.site.register(Eventos, EventosAdmin)
