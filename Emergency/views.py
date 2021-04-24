from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def MainPage(request):
	return HttpResponse('<html><title>Call an Emergency</title><h1 style="color:red">Call for Emergency now</h1><input type="text" id="newEntry" name="Entry1" placeholder="Send your location!&#063">&nbsp<input type="submit" value="Confirm"></html>')
