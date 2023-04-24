from django.contrib import admin
from menu.models import Menu, MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'menu', 'url']


admin.site.register(Menu)
admin.site.register(MenuItem, MenuItemAdmin)
