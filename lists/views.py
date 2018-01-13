from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
	

	if request.method == 'POST':
		new_item_text = request.POST.get('item_text', '')
		# shortcut, no need to call save()
		Item.objects.create(text=new_item_text)
	# else:
	# 	new_item_text = ''


	# we don't need the arguments version at the bottom because
	# the POST-REDIRECT-GET process is automatically done by browser
		return redirect('/')

	# ORM operations
	# item = Item()
	# item.text = request.POST.get('item_text', '')
	# item.save()


	# return HttpResponse('<html><title>To-Do Lists</title></html>')
	# Now we don't have to generate response ourself.
	# Render method woud automatically search inside current app's templates folder
	# and build a response for you (based on the content of the template)
	return render(request, 'home.html')

	# !!! the above render won't success if you app is not registered yet
	# MAKE SURE check variable INSTALLED_APPS in core/settings.py

	# render arguments version
	# request.POST is a dictionary like object supporting multi-valued key as well
	# return render(request, 'home.html', {
	# 		'new_item_text': new_item_text
	# 	})