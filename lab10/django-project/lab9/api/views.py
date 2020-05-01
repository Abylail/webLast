from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest


# Create your views here.
def companies_list(request):
    return HttpResponse('hi')

