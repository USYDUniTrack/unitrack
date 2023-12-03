from django.http import HttpResponse
import datetime
from django.shortcuts import render


def main_page(request):
    contex = {}
    return render(request, 'index.html', contex)
