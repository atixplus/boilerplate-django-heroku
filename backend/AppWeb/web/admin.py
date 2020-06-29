from django.contrib import admin
from .models import State
# Register your models here.
class StateAdmin(admin.ModelAdmin):
  list_display = ('user', 'event', 'timestamp')
  
admin.site.register(State, StateAdmin)