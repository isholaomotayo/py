# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from .models import Album


# Create your views here.
def index(request):
    all_albums = Album.objects.all()
    html = '<h1> Welcome to Music </h1> <br><style> img { margin:10px ; float:left;  display: inline-block;} </style>'
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + '<img width=200 src="' + album.album_logo + '"/>' + '</a>'
    return HttpResponse(html)


def detail(request, album_id):
    return HttpResponse("<h2> Details for Album ID: " + str(album_id) + "</h2>")
