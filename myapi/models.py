from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    updated = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    

    def __str__(self):
        return self.first_name