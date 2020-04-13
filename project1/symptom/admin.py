from django.contrib import admin
from symptom.models import log, contact
from symptom.models import registeration


admin.site.register(log)
admin.site.register(registeration)

admin.site.register(contact)

# Register your models here.
