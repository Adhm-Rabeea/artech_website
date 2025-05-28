from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=100)  # كود الأيقونة (اختياري)
    
    def __str__(self):
        return self.title