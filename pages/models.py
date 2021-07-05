from django.db import models

# Create your models here.
class Team(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    designation=models.CharField(max_length=100)
    profile_img=models.ImageField(upload_to='team/%Y/%m/%d')
    hire_date=models.DateField(auto_now_add=True)
    facebook_link=models.URLField(max_length=100, blank=True)
    twitter_link=models.URLField(max_length=100, blank=True)
    insta_link=models.URLField(max_length=100)

    def __str__(self):
        return self.first_name.capitalize() +" "+ self.last_name.capitalize()
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=500)
    phone=models.CharField(max_length=20)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Contact'
        verbose_name_plural='Contacts'

