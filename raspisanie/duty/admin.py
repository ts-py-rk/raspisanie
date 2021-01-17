from django.contrib import admin
from . models import Calendar, Month, People, SuperDuty


admin.site.register(Calendar)
admin.site.register(Month)
admin.site.register(People)
admin.site.register(SuperDuty)

# class Month(admin.ModelAdmin):
#     list_display = ("day", "person")