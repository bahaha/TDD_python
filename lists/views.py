from django.shortcuts import render, redirect

from django.http import HttpResponse

from lists.models import Item

# Create your views here.
def homepage(request):
	if request.method == 'POST':
		item = Item()
		item.text = request.POST.get('item_text', '')
		item.save()
		return redirect('/lists/the-only-list-in-the-world/')
	return render(request, 'index.html')

def view_list(request):
	items = Item.objects.all()
	return render(request, 'list.html', {
		'items': items
	})

def new_list(request):
	Item.objects.create(text=request.POST['item_text'])
	return redirect('/lists/the-only-list-in-the-world/')