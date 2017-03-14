from django.conf.urls import url
from views import CreatePeople, ListPeople, DeletePeople
urlpatterns = [
	url(r'^create', CreatePeople.as_view()),
	url(r'^delete/(?P<people_id>[0-9]+)$', DeletePeople.as_view()),
	url(r'^', ListPeople.as_view()),
]
