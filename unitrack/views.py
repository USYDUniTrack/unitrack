from django.shortcuts import render


def main_page(request):
    contex = {}
    return render(request, 'index.html', contex)


def hx_main_page(request):
    contex = {}
    return render(request, 'index.html', contex)


def timetable(request):
    contex = {}
    return render(request, 'timetable.html', contex)


def about_us(request):
    contex = {}
    return render(request, 'about_us.html', contex)


def friends(request):
    contex = {}
    return render(request, 'friends.html', contex)

def sign_in(request):
    contex = {}
    return render(request, 'sign_in.html', contex)

def register(request):
    contex = {}
    return render(request, 'register.html', contex)
