from django.contrib import admin
from django import forms
from .models import*


class RouteAdminForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'
        widgets = {
            'info': forms.CheckboxSelectMultiple,  # Заменяем стандартный виджет на чекбоксы
        }

class RouteAdmin(admin.ModelAdmin):
    form = RouteAdminForm


admin.site.register(Info)
admin.site.register(Phrases)
admin.site.register(Route, RouteAdmin)
admin.site.register(Maps)