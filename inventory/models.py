# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Laboratory(models.Model):
	lab_name = models.CharField("Laboratory Name", max_length=200)
	lab_incharge = models.CharField("Laboratory Incharge", max_length=200)
	def __str__(self):
		return self.lab_name

	class Meta:
		verbose_name = "Laboratory"
		verbose_name_plural = "Laboratories"

class Item(models.Model):
	lab = models.ForeignKey(Laboratory, on_delete=models.CASCADE)
	item_name = models.CharField("Item Name", max_length=200)
	item_count = models.IntegerField("Count", default=0)
	item_cost = models.DecimalField("Cost (In INR)", max_digits=10, decimal_places=2)
	total_cost = models.DecimalField("Total Cost (In INR)", max_digits=10, decimal_places=2)
	def save(self, *args, **kwargs):
		self.total_cost = self.item_count*self.item_cost

		return super(Item, self).save(*args, **kwargs)

	def __str__(self):
		return self.item_name