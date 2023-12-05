from django.shortcuts import render


def main_page(request):
    contex = {}
    return render(request, 'index.html', contex)


def unit_search(request):
    contex = {}
    return render(request, 'unit_search.html', contex)


def unit_page(request, unit_code):
    contex = {'unit_code': unit_code}
    return render(request, 'unit_page.html', contex)
