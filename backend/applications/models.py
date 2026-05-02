from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Application(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'), 
        ('oa', 'Online Assessment'), 
        ('interview', 'Interview'),
        ('rejected', 'Rejected'),
        ('offer', 'Offer'),
    ]

    user = models.ForeignKey(User, on_delete= models.CASCADE)

    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    status = models.CharField(
        max_length=20, 
        choices=STATUS_CHOICES,
        default='applied'
    )

    date_applied = models.DateField()
    deadline = models.DateField(null=True, blank=True)

    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company} - {self.role}"

