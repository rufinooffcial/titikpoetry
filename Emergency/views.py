from django.http import HttpResponse
from Emergency.models import Item
from django.shortcuts import render, redirect


def MainPage(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['Newmember'])
		return redirect('/Emergency/viewlist_url/')
	#return render(request,'mainpage.html')
	items = Item.objects.all()
	return render(request, 'mainpage.html', {'newPerson': items})

def ViewList(request):
		items = Item.objects.all()
		return render(request, 'mainpage.html', {'newPerson': items})