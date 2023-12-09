from django.shortcuts import render

def main_page(request):
    contex = {}
    return render(request, 'index.html', contex)



    





