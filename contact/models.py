from django.db import models
from datetime import  datetime
# Create your models here.
class Inquery(models.Model):
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    car_title=models.CharField(max_length=100,default="Unknown")
    customer_need= models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=15)
    message=models.TextField(blank=True)
    user_id=models.PositiveIntegerField(blank=True)
    created_date=models.DateTimeField(blank=True,default=datetime.now)

    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name='Inquery'
        verbose_name_plural='Inqueries'



