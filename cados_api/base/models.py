from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name

class Advocate(models.Model):
    username = models.CharField(max_length=100)
    bio = models.TextField(max_length=500, null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)
    # email = models.EmailField()
    # phone = models.CharField(max_length=15)
    # address = models.TextField()
    # city = models.CharField(max_length=100)
    # state = models.CharField(max_length=100)
    # country = models.CharField(max_length=100)
    # zipcode = models.CharField(max_length=10)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.username