from django.shortcuts import render
from models import get_nav_list, get_categories

# Create your views here.
def index(request):
	nav = get_nav_list()
	return render(request, "blog/index.html", {
		"header":"Start Bootstrap",
		"nav":nav,
		"categories":get_categories()
		})