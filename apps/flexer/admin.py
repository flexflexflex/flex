from django import forms
from django.contrib import admin

from .models import FlexUser, Flex


class FlexModelForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea, max_length=120)

    class Meta:
        model = Flex
        fields = "__all__"


@admin.register(FlexUser)
class FlexUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'token']
    filter_horizontal = ['followed']


@admin.register(Flex)
class FlexAdmin(admin.ModelAdmin):
    form = FlexModelForm
    filter_horizontal = ['members']
    list_display = ['owner', 'title', 'description']

