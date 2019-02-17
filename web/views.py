from django.shortcuts import render

from django.shortcuts import render
from django.shortcuts import render, HttpResponse

def inicio(request):
	return render(request, "base.html", {})