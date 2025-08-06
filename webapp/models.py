from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    age = models.CharField(max_length=15, blank=True, null=True)
    team = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class form_email(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='form')
    t_email=models.CharField(max_length=100, blank=True, null=True)
    email_ids = models.TextField()  # Store emails as a comma-separated string
    subject =models.CharField(max_length=5000, blank=True, null=True)
    body = models.TextField(null=True)
    pdfs = models.FileField(upload_to='emp_documents/', blank=True, null=True)
    password= models.CharField(max_length=100,blank=True, null=True)
    def get_email_list(self):
        return self.email_ids.split(',')

    def __str__(self):
        return f"{self.user.username} - {self.email_ids}"
