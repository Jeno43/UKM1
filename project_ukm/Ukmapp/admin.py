from django.contrib import admin
from .models import Ukmapp, Sportukmapp, RegistrationData, DataBarang,DataKaryawan

# Register your models here.

admin.site.register(Ukmapp)
admin.site.register(Sportukmapp)
admin.site.register(RegistrationData)
admin.site.register(DataBarang)
admin.site.register(DataKaryawan)
