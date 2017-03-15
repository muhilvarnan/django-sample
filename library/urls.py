from django.conf.urls import url
from views import BookCreateListView,BookRetrieveUpdateDeleteView,AuthorCreateListView,AuthorRetrieveUpdateDeleteView
urlpatterns = [
	url(r'^book$', BookCreateListView.as_view()),
	url(r'^book/(?P<pk>.*)$', BookRetrieveUpdateDeleteView.as_view()),
	url(r'^author$', AuthorCreateListView.as_view()),
	url(r'^author/(?P<author_id>.*)$',AuthorRetrieveUpdateDeleteView.as_view()),
]
