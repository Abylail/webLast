from django.db import models
from companies.models import company


# Create your models here.
class vacancy(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    salary = models.FloatField()
    company = models.ForeignKey(company, on_delete=models.CASCADE, related_name='vacancy')

    def to_Json(self):
        return{
            'id' : self.id,
            'name': self.name,
            'salary': self.salary,
            'company': self.company.name
        }
