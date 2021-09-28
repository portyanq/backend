from django.contrib import admin

from . import models


@admin.register(models.Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    fields = ['name', 'url', 'img']


@admin.register(models.Ready)
class ReadyAdmin(admin.ModelAdmin):
    list_display = ('person', 'percent')
    fields = ['percent', 'person', 'mark01', 'mark02', 'mark03', 'mark04', 'mark05', 'mark06', 'report']


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('personName', 'textReview', 'date')


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'second_name', 'phone', 'date_joined')
    list_filter = ('date_joined', 'last_login')
    fields = [('first_name', 'second_name'),('email', 'phone'),'password', ('last_login', 'date_joined'), ('is_superuser', 'is_staff', 'is_active'), 'groups', 'user_permissions']


@admin.register(models.FormData)
class FormDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'phone', 'mail')
    
