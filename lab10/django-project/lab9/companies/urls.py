from django.urls import path
from companies.views import company_by_id, comp_vacan, companies_list

urlpatterns = {
    path('', companies_list),
    path('<int:comp_id>/', company_by_id),
    path('<int:comp_id>/vacancies/', comp_vacan),
}