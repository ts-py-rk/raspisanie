from django.contrib import admin
from . models import Calendar, Month, People, SuperDuty, Static, Article, Comment


# admin.site.register(Calendar)
admin.site.register(Month)
admin.site.register(People)
admin.site.register(SuperDuty)
admin.site.register(Static)


admin.site.register(Article)
admin.site.register(Comment)