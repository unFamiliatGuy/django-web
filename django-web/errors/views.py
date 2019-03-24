from django.shortcuts import render
from django.http import HttpResponseForbidden, HttpResponseBadRequest, HttpResponse

def error_401(request):
    return HttpResponse(status='401')

def error_400(request):
    return HttpResponseBadRequest()

def error_403(request):
    return HttpResponseForbidden()