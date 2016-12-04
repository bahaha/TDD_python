from django.shortcuts import render, redirect

from django.http import HttpResponse

from lists.models import Item

# Create your views here.
def homepage(request):
	if request.method == 'POST':
		item = Item()
		item.text = request.POST.get('item_text', '')
		item.save()
		return redirect('/')
	return render(request, 'index.html', {
		'items': Item.objects.all()
	})