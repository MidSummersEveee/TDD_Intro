from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_page(request):
	# return HttpResponse('<html><title>To-Do Lists</title></html>')
	# Now we don't have to generate response ourself.
	# Render method woud automatically search inside current app's templates folder
	# and build a response for you (based on the content of the template)
	return render(request, 'home.html')

	# !!! the above render won't success if you app is not registered yet
	# MAKE SURE check variable INSTALLED_APPS in core/settings.py