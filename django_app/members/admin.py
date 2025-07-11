from django.contrib import admin

from .models import Member


# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email')
    search_fields = ('firstname', 'lastname', 'email')
    list_filter = ('firstname', 'lastname', 'email')
    ordering = ('firstname', 'lastname')