from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from vacancies.models import vacancy

# Create your views here.
def vacancies_list(request):
    vacancies = vacancy.objects.all()
    vac_json = [i.to_Json() for i in vacancies]
    return JsonResponse(vac_json, safe=False)

def vacancies_byid(request, vacan_id):
    vac = vacancy.objects.get(id=vacan_id)
    vac_json = vac.to_Json()
    return JsonResponse(vac_json, safe=False)

def top_three(request):
    vac = vacancy.objects.order_by('-salary')[:3]
    vac_json = [v.to_Json() for v in vac]
    return JsonResponse(vac_json, safe=False)
