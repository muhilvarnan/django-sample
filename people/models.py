from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Person(models.Model):
	"""
	person model
	"""
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	age = models.IntegerField(default=0)


def create_people(data):
	"""
	create people
	"""
	try:
		Person.objects.create(first_name=data.get("first_name"), last_name = data.get("last_name"), age= data.get("age"))
		return "Added successfully"
	except Exception, e:
		print e
		return "Error in adding"


def get_people_list():
	"""
	get people list
	"""
	try:
		return Person.objects.all().values()
	except Exception, e:
		print e
		return []

def delete_people(people_id):
	"""
	delete people
	"""
	try:
		personObj = Person.objects.get(id=people_id)
		personObj.delete()
		return True
	except Exception, e:
		print e
		return False