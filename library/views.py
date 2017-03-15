from django.shortcuts import render
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from serializers import BookSerializer,AuthorSerializer
from models import Book,Author
# Create your views here.

class BookCreateListView(generics.ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class BookRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
	queryset = Book.objects.all()			
	serializer_class = BookSerializer

class AuthorCreateListView(generics.GenericAPIView):
	serializer_class = AuthorSerializer

	def get(self,request):
		author_list = Author().get_author_list(request)
		print "*******"
		print author_list
		print "********"
		return Response(author_list,status=status.HTTP_200_OK)

	def post(self,request):
		response = Author().create_author(request)
		return Response({"details":response.get("details")},status=response.get("status_code"))

class AuthorRetrieveUpdateDeleteView(generics.GenericAPIView):
	serializer_class = AuthorSerializer

	def get(self,request,author_id):
		result = Author().get_author(author_id)	
		return Response(result.get("details"),status=result.get('status_code'))

	def put(self,request,author_id):
		result = Author().update_author(request,author_id)
		return Response(result.get("details"),status=result.get('status_code'))	

	def delete(self,request,author_id):
		result = Author().delete_author(author_id)
		return Response(result.get("details"),status=result.get('status_code'))		