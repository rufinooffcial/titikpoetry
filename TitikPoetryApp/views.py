from django.http import HttpResponse
from TitikPoetryApp.models import Item, Recruit
from django.shortcuts import render, redirect

def MainPage(request):
	return render(request, 'Titikpoetry.html')

def NewList(request):
	# RecId = Recruit.objects.create()
	RecId = Recruit.objects.create(
		name=request.POST['member'],
		contact=request.POST['contact'],
		sex=request.POST['Sex'],
		title=request.POST['Title'],
		link=request.POST['Link'],
		)
	return redirect(f'/TitikPoetryApp/{RecId.id}/')
def ViewList(request, RecId):
	RecId = Recruit.objects.get(id=RecId)
	return render(request, 'TitikTheSecond.html', {'RecId': RecId})

def AddItem(request,rId):
	rId = Recruit.objects.get(id=rId)
	Item.objects.create(RecId=rId,
		username=request.POST['Newmember'], 
		title_tula=request.POST['title_tula'],
		video_file=request.POST['file'])
	return redirect(f'/TitikPoetryApp/{rId.id}/')

def Login(request):
	RecId=Login.objects.create(
	username=request.POST['Newmember'],
	password=request.POST['title_tula'])
	return render(request, 'TitikTheSecond.html')

def Dmin(request):
	RecId=Dmin.objects.create(
	username=request.POST['Newmember'],
	password=request.POST['title_tula'])
	return redirect(f'/TitikPoetryApp/')

def Admindoing(request):
	publications=Admindoing.objects.create(
	username=request.POST['Newmember'],
	password=request.POST['title_tula'])
	return redirect(f'/TitikPoetryApp/')




	#if request.method == 'POST':
		#Item.objects.create(text=request.POST['Newmember'])
		#return redirect('/Emergency/viewlist_url/')
