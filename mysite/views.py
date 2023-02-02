from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
import json

def home_view(request):
	# t = loader.get_template('parser.html')
	# html = t.render()
	# return HttpResponse(html)
	dic = {}
	return render(request, 'home.html', dic)

def flash_info_view(request):
	# t = loader.get_template('parser.html')
	# html = t.render()
	# return HttpResponse(html)
	dic = {}
	return render(request, 'flash_info.html', dic)

def mp_info_view(request):
	# t = loader.get_template('parser.html')
	# html = t.render()
	# return HttpResponse(html)
	dic = {}
	return render(request, 'mp_info.html', dic)

def mp_test_view(request):
	project = ['project_1','project_2','project_3']
	return render(request, 'mp_test.html', {'size': 3,'project':json.dumps(project)})