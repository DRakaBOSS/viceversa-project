from django.http import HttpResponse
from django.shortcuts import render

def viceversa(request):
	return render(request, 'viceversa.html')