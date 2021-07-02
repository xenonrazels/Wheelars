from django.db import models
from multiselectfield import MultiSelectField
from ckeditor.fields import RichTextField
# Create your models here
from datetime import datetime

class car(models.Model):
    STATE_CHOICES=[
        ('Provience No.1','Provience No. 1'),
        ('Provience No.2 ','Provience No. 2'),
        ('Bagmati Provience','Bagamati Provience'),
        ('Lumbini Provience','Lumbini Provience'),
        ('Karnali Provience','Karnali Provience'),
        ('Sudarpashim Provience','Sudurpaschim Provience'),
    ]
    YEAR=[]
    for i in range(2000 , (datetime.now().year+1)):
        YEAR.append((i,i))

    FEATURE_CHOICES = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
        ('Automatic Headlights','Automatic Headlights')
    )
#     list=[
#         Adaptive Cruise Control
#         Airbags
#         Air Conditioning
#         Alarm System
#         Anti - theft Protection
#         Audio Interface
#         Automatic Climate Control
#
#         Auto Start / Stop
#         Bi - Xenon Headlights
#         Audio Interface
#         Bluetooth Handset
#         BOSE Surround Sound
#         Burmester Surround Sound
#         CD / DVD Autochanger
#         CDR Audio
#         Cruise Control
#         Direct Fuel Injection
#         Electric Parking Brake
#         Floor Mats
#         Garage Door Opener
#         Leather Package
#         Locking Rear Differential
#         Luggage Compartments
#         Manual Transmission
#         Navigation Module
#         Online Services
#         ParkAssist
#         Porsche Communication
#         CD / DVD Autochanger
#         Power Steering
#         Reversing Camera
#         Roll - over Protection
#         Seat Heating
#         Seat Ventilation
#         Sound Package Plus
#         Sport Chrono Package
#         Steering Wheel Heating
#         Tire Pressure Monitoring
#         Universal Audio Interface
#         Voice Control System
#         Wind Deflector
# a
#     ]

    DOOR_CHOICES = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )
    car_title=models.CharField(max_length=100)
    states=models.CharField(max_length=100, choices=STATE_CHOICES)
    city=models.CharField(max_length=100,default='none')
    years=models.IntegerField(choices=YEAR)
    features=MultiSelectField(choices=FEATURE_CHOICES)
    doors=models.CharField(choices=DOOR_CHOICES,max_length=100)
    passenger=models.PositiveIntegerField()
    model=models.CharField(max_length=100)
    price=models.IntegerField()
    milege=models.IntegerField()
    miles=models.PositiveIntegerField()
    description=RichTextField()
    interior=models.CharField(max_length=100)
    condition=models.CharField(max_length=100)
    tumbnail_img =models.ImageField(upload_to='cars/%Y/%m/%d')
    pic_front=models.ImageField(upload_to='cars/%Y/%m/%d')
    pic_back=models.ImageField(upload_to='cars/%Y/%m/%d')
    pic_left=models.ImageField(upload_to='cars/%Y/%m/%d')
    pic_right=models.ImageField(upload_to='cars/%Y/%m/%d')
    body_style=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    fuel_type=models.CharField(max_length=100)
    is_featured=models.BooleanField(default=False)
    no_of_passed_owners=models.IntegerField()
    transmission=models.CharField(max_length=100)
    engine=models.CharField(max_length=100)
    vin_number=models.CharField(max_length=100,blank=True)
    created_date=models.DateField(default=datetime.now,blank=True)
    brand=models.CharField(max_length=100,default='Unknown')
    vehicle_type=models.CharField(max_length=100,default='Unknown')
    discount_percent=models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.car_title

