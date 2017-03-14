from django.shortcuts import render, redirect
from django.views import View
from .models import create_people, get_people_list, delete_people
# Create your views here.

class CreatePeople(View):

	def get(self, request):
		ct = {
			"title":"Create people"
		}
		return render(request, "people/create.html")

	def post(self, request):
		print request.POST
		ct = {
			"title":"Create people",
			"message":create_people(request.POST)
		}
		return render(request, "people/create.html", ct)

class ListPeople(View):

	def get(self, request):
		ct = {
			"title":"List People",
			"people":get_people_list()
		}
		return render(request, "people/list.html", ct)

class DeletePeople(View):

	def get(self, request, people_id):
		print "omcm"
		delete_people(people_id)
		return redirect("/people")
