from django.db import models

# Create your models here.
class Team(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    designation=models.CharField(max_length=100)
    profile_img=models.ImageField(upload_to='media/team/%Y/%m/%d')
    hire_date=models.DateField(auto_now_add=True)
    facebook_link=models.URLField(max_length=100, blank=True)
    twitter_link=models.URLField(max_length=100, blank=True)
    insta_link=models.URLField(max_length=100)

    def __str__(self):
        return self.first_name.capitalize() +" "+ self.last_name.capitalize()