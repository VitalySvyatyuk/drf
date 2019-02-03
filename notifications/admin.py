from django.contrib import admin

from .models import Template, Office

class TemplateAdmin(admin.ModelAdmin):
    pass


class OfficeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Template, TemplateAdmin)
admin.site.register(Office, OfficeAdmin)
