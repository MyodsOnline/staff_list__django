from django.contrib import admin

from .models import Staff, Substation, Organization


# class StaffAdmin(admin.ModelAdmin):
#     list_display = ('first_name', 'last_name',)


admin.site.register(Staff)
admin.site.register(Substation)
admin.site.register(Organization)
