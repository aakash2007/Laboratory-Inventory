# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from models import *

from django.template import loader

from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


import csv
import xlsxwriter, StringIO

def index(request):
	template = loader.get_template('inventory/index.html')
	return render(request, 'inventory/index.html')

@staff_member_required
def LabExcel(request, **kwargs):
	lab = Laboratory.objects.all()
	output = StringIO.StringIO()
	workbook = xlsxwriter.Workbook(output)
	bold = workbook.add_format({'bold': True})
	for l in lab:
		worksheet = workbook.add_worksheet(l.lab_name)
		worksheet.write(0,0, "Laboratory:", bold)
		worksheet.write(0,1, l.lab_name)
		worksheet.write(1,0, "Incharge:", bold)
		worksheet.write(1,1, l.lab_incharge)
		worksheet.write(2,0, "Item List", bold)
		worksheet.write(3,0, "Name", bold)
		worksheet.write(3,1, "Count", bold)
		worksheet.write(3,2, "Cost", bold)
		worksheet.write(3,3, "Total Cost", bold)
		items = l.item_set.all()
		for i, it in enumerate(items):
			worksheet.write(i+4,0, it.item_name)
			worksheet.write(i+4,1, it.item_count)
			worksheet.write(i+4,2, it.item_cost)
			worksheet.write(i+4,3, it.total_cost)

	workbook.close()
	filename = 'Lab Inventory.xlsx'
	output.seek(0)
	response = HttpResponse(output.read(), content_type="application/ms-excel")
	response['Content-Disposition'] = 'attachment; filename=%s' % filename
	return response