from django.urls import path
from vacancies.views import vacancies_list, vacancies_byid, top_three

urlpatterns = [
    path('', vacancies_list),
    path('<int:vacan_id>/', vacancies_byid),
    path('top_three/', top_three),
]