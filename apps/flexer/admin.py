from django.contrib import admin

from .models import FlexUser, Flex


@admin.register(FlexUser)
class FlexUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'token']
    filter_horizontal = ['followed']


@admin.register(Flex)
class FlexAdmin(admin.ModelAdmin):
    filter_horizontal = ['members']
    list_display = ['owner', 'description']

