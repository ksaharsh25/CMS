from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display=['created_at','modified_at']