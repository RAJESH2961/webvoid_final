from django.db import models

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    mobile = models.PositiveIntegerField(blank=True, null=True)
    subject = models.CharField(max_length=100, blank=False, null=False)
    message = models.CharField(max_length=1000, blank=False, null=False)

    def __str__(self):
        return f"Name: {self.name} , Email: {self.email}, Phone: {self.mobile}"


class Services(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='services_images', null= False, blank= False)
    description = models.CharField(max_length=1000)
    status = models.BooleanField(default=False, help_text="0-show, 1-Hidden")
    # slug = models.SlugField(default="", null=False)


    def __str__(self):
        return f"Title: {self.title} "

class Service_detail(models.Model):
    name = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='services')
    image = models.ImageField(upload_to='services_images/service_details', null= False, blank= False)
    description = models.CharField(max_length=1000)
    status = models.BooleanField(default=False, help_text="0-show, 1-Hidden")
    techstack= models.CharField(max_length=1000)
    languages_used=models.CharField(max_length=100)


    def __str__(self):
        return f"Name: {self.name} ,  Tech: {self.techstack}"

