from __future__ import unicode_literals
from rest_framework import status
from django.db import models
import uuid

# Create your models here.

class Book(models.Model):
	"""
	Book - Model
	"""
	STATUS_CHOICES = (
		('AVAILABLE','AVAILABLE'),
		('NOT_AVAILABLE','NOT_AVAILABLE')
		)
	uuid = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
	name = models.CharField(max_length=255)
	description = models.TextField(null=True)
	author = models.ForeignKey('author')
	status = models.CharField(choices=STATUS_CHOICES,max_length=255)
	created_datetime = models.DateTimeField(auto_now_add=True)
	modified_datetime = models.DateTimeField(auto_now=True)

class Author(models.Model):
	"""
	Author of the books
	"""
	uuid = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
	first_name = models.CharField(max_length=255,null=True,blank=True)
	last_name = models.CharField(max_length=255,null=True,blank=True)
	age = models.IntegerField(null=True)
	phone = models.CharField(max_length=255)

        def get_author_list(self,request):
            from serializers import AuthorSerializer
    	    try:
		author_list = Author.objects.all()
		author_list_data = AuthorSerializer(author_list,many=True)
		return author_list_data.data
	    except Exception,e:
		print e
		return []

   	def create_author(self,request):
	    try:
		author_obj = Author()
		author_obj.first_name = request.data.get("first_name")
		author_obj.last_name = request.data.get("last_name")
		author_obj.age = request.data.get("age")
		author_obj.phone = request.data.get("phone")
		author_obj.save()
		return {
		"details":"Author Created Successfully",
		"status_code":status.HTTP_200_OK
		}
            except Exception,e:
		print e
		return {
		"details":str(e),
		"status_code":status.HTTP_500_INTERNAL_SERVER_ERROR
		}

        def get_author(self,author_id):
	    from serializers import AuthorSerializer
            try:
		author_obj = Author.objects.get(uuid=author_id)
                author_data = AuthorSerializer(author_obj).data
                return {
			"details":author_data,
               		"status_code":status.HTTP_200_OK
			}
	    except Author.DoesNotExist:
		return {
			"details":"Invalid Author Id",
			"status_code":status.HTTP_400_BAD_REQUEST
			}
            except Exception,e:
		print e
		return {
		"details":str(e),
		"status_code":status.HTTP_500_INTERNAL_SERVER_ERROR
		}

	def update_author(self,author_id):
	    try:
		author_obj = Author.objects.get(uuid=author_id)
		author_obj.first_name = request.data.get("first_name")
		author_obj.last_name = request.data.get("last_name")
		author_obj.age = request.data.get("age")
		author_obj.phone = request.data.get("phone")
		author_obj.save()
		return {
		"details":"Author Updated Successfully",
		"status_code":status.HTTP_200_OK
		}
	    except Author.DoesNotExist:
		return {
			"details":"Invalid Author Id",
			"status_code":status.HTTP_400_BAD_REQUEST
		}
            except Exception,e:
		print e
		return {
		"details":str(e),
		"status_code":status.HTTP_500_INTERNAL_SERVER_ERROR
		}

	def delete_author(self,author_id):
	    try:
              Author.objects.get(uuid=author_id).delete()
	      return {
		"details":"Author Deleted successfully",
		"status_code":status.HTTP_200_OK
		}
	    except Author.DoesNotExist:
		return {
			"details":"Invalid Author Id",
			"status_code":status.HTTP_400_BAD_REQUEST
            		}
            except Exception,e:
		print e
		return {
		"details":str(e),
		"status_code":status.HTTP_500_INTERNAL_SERVER_ERROR
		}


