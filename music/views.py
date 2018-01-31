from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.http import Http404


def index(request):
	all_albums=Album.objects.all()
	# html=''
	# for album in all_albums:
	# 	url='/music/'+ str(album.id)+ '/'
	# 	html+='<a href="' + url + '">'+ album.album_title + '</a><br>'
	# return HttpResponse(html)
	
	return render(request,'music/index.html',{'all_albums':all_albums})

def detail(request,album_id):
	try:
		album=Album.objects.get(pk=album_id)
	except Album.DoesNotExist:
		raise Http404("Album doesNotExist")	
	return render(request,'music/detail.html',{'album':album})
