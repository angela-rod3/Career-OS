from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recruiter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    linkedin = models.URLField(blank=True)

    last_contacted = models.DateField(null=True, blank=True)
    follow_up_date = models.DateField(null=True, blank=True)

    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.company})"
    