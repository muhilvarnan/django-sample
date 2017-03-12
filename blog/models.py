from __future__ import unicode_literals

from django.db import models

# Create your models here.

def get_nav_list():
	"""
	get nav list
	"""
	return [
		"about",
		"services",
		"contact"
	]

def get_categories():
	return [
		{
		"id":1,
		"name":"Category 1"
		},
		{
		"id":2,
		"name":"Category 2"
		},
		{
		"id":3,
		"name":"Category 3"
		},
		{
		"id":4,
		"name":"Category 4"
		},
		{
		"id":5,
		"name":"Category 5"
		},
	]

class Category(models.Model):
	"""
	category
	"""
	name = models.CharField(max_length=255)

class Blog(models.Model):
	"""
	blog model
	"""
	name = models.CharField(max_length=255)
	content = models.TextField()
	created_time = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey(Category)