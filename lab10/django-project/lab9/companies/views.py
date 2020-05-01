from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest

from companies.models import company
from vacancies.models import vacancy

# Create your views here.
def companies_list(request):
    companies = company.objects.all()

    json_comp = [i.to_Json() for i in companies]

    return JsonResponse(json_comp, safe=False)

def company_by_id(request, comp_id):
    comp = company.objects.get(id=comp_id)
    jsoncomp = comp.to_Json()
    return JsonResponse(jsoncomp, safe=False)


def comp_vacan(request, comp_id):
    vacancies = vacancy.objects.all()
    vac_tojson = []
    for i in vacancies:
        if i.company.id == comp_id:
            ij = i.to_Json()
            vac_tojson.append(ij)
    return JsonResponse(vac_tojson, safe=False)

