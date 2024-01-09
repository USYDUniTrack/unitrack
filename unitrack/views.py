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


def about_us(request):
    contex = {}
    return render(request, 'about_us.html', contex)


def friends(request):
    contex = {}
    return render(request, 'friends.html', contex)

