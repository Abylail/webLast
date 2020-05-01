from django.db import models

# Create your models here.
class company(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    city = models.CharField(max_length=15)
    address = models.TextField()

    def to_Json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address,
        }