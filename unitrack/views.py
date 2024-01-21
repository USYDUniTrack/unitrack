from django.shortcuts import render

def main_page(request):
    contex = {}
    return render(request, 'index.html', contex)


def timetable(request):
    contex = {}
    return render(request, 'timetable.html', contex)


def degree_plan(request):
    contex = {}
    return render(request, 'degree_plan.html', contex)


def sign_in(request):
    contex = {}
    return render(request, 'sign_in.html', contex)

def register(request):
    contex = {}
    return render(request, 'register.html', contex)