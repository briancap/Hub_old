from django.http import HttpResponse
from django.shortcuts import render
from integration.connector.FileConnector import DelimitedFile

# Create your views here.
def index(request):
    delimFile = DelimitedFile()
    return HttpResponse("Hello, world: " + delimFile.getConnection() )
