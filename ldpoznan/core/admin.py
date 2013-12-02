from django.contrib import admin
from core.models import Registration

class RegistrationAdmin(admin.ModelAdmin):
	list_display = ('name', 'mail', 'info', 'time_created')

admin.site.register(Registration, RegistrationAdmin)