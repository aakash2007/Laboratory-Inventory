# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
# Register your models here.

class ItemInline(admin.TabularInline):
	model = Item
	extra = 0

class ItemAdmin(admin.ModelAdmin):
	fields = ['item_name', 'item_count']
	search_fields = ['item_name']
	list_display = ['item_name', 'item_count']

class LaboratoryAdmin(admin.ModelAdmin):
	fields = ['lab_name', 'lab_incharge']
	inlines = [ItemInline]
	list_display = ('lab_name', 'lab_incharge')
	search_fields = ['lab_name']


admin.site.register(Laboratory, LaboratoryAdmin)
admin.site.register(Item, ItemAdmin)