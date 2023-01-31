from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def home_view(request):
	# t = loader.get_template('parser.html')
	# html = t.render()
	# return HttpResponse(html)
	dic = {}
	return render(request, 'home.html', dic)

def flash_info__view(request):
	# t = loader.get_template('parser.html')
	# html = t.render()
	# return HttpResponse(html)
	dic = {}
	return render(request, 'flash_info.html', dic)

def mp_info__view(request):
	# t = loader.get_template('parser.html')
	# html = t.render()
	# return HttpResponse(html)
	dic = {}
	return render(request, 'mp_info.html', dic)