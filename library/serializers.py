from rest_framework import serializers
from models import Book,Author

class BookSerializer(serializers.ModelSerializer):
	author_name = serializers.SerializerMethodField('get_author_fullname')
	class Meta:
		model = Book
		fields = ('uuid','name','author','author_name','description','status')

	def get_author_fullname(self,obj):
		return obj.author.first_name+" "+obj.author.last_name

class AuthorSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Author
		fields = ('uuid','first_name','last_name','age','phone')

	
