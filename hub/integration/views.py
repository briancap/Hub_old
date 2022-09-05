from django.http import HttpResponse
from django.shortcuts import render
from integration.connector.FileConnector import DelimitedFileConnector

# Create your views here.
def index(request):
    delimFile = DelimitedFileConnector()
    delimFile.importAccounts()
    return HttpResponse("Hello, world: " )
