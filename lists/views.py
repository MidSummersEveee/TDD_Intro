from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
def home_page(request):
	

	# if request.method == 'POST':
		# shortcut, no need to call save()
		# Item.objects.create(text=request.POST.get('item_text', ''))
	# else:
	# 	new_item_text = ''

	# we don't need the arguments version at the bottom because
	# the POST-REDIRECT-GET process is automatically done by browser
		# return redirect('/lists/the-only-list-in-the-world/')

	# ORM operations
	# item = Item()
	# item.text = request.POST.get('item_text', '')
	# item.save()

	# not going to use because we leave that part to other views
	# items = Item.objects.all()
	# return render(request, 'home.html', {'items': items})

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

def view_list(request, list_id):
	list_ = List.objects.get(id=list_id)
	# items = Item.objects.filter(list=list_)
	# return render(request, 'list.html', {'items': items})
	return render(request, 'list.html', {'list': list_})

def new_list(request):
	if request.method == 'POST':
		list_ = List.objects.create()
		# shortcut, no need to call save()
		Item.objects.create(text=request.POST.get('item_text', ''), list=list_)
		return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
	list_ = List.objects.get(id=list_id)
	Item.objects.create(text=request.POST.get('item_text', ''), list=list_)
	return redirect(f'/lists/{list_.id}/')