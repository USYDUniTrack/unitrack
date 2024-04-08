from django.http.response import HttpResponseNotFound
from django.shortcuts import render

# Create your views here.

from .models import Units
from .forms import DegreeForm

units = ["COMP2017", "COMP2123", "COMP3027"]

def unit_search(request):
    contex = {'units': units}
    return render(request, 'unit_search.html', contex)


def hx_unit_search(request):
    contex = {'units': units}
    return render(request, 'components/unit_search.html', contex)


def unit_page(request, unit_code: str):

    unit = Units.objects.filter(unit_code=unit_code).first()

    if(unit):
        contex = {'unit_code': unit.unit_code, "unit_name": unit.unit_name}
        return render(request, 'unit_page.html', contex)

    elif unit_code != unit_code.upper():
        return redirect(f"/units/{unit_code.upper()}")

    else:
        return HttpResponseNotFound("Unit not found")


def degree_plan(request):
    form = DegreeForm()
    contex = {'form': form}
    return render(request, 'degree_plan.html', contex)


def hx_degree_plan(request):
    form = DegreeForm()
    contex = {'form': form}
    return render(request, 'components/degree_plan.html', contex)
