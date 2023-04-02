from django.db import models
from django.utils import timezone
from datetime import date
from django.utils.translation import gettext as _
# Create your models here.

SPORT = (
    ('carrom','carrom'),
    ('chess','chess'),
    ('cricket','cricket'),
)

POSITION = (
    ('winner','winner'),
    ('runner up','runner up'),
)

CATEGORY = (
    ('senior','senior'),
    ('junior','junior'),
    ('sub junior','sub junior'),
)

GENDER = (
    ('male','male'),
    ('female','female'),
)

STATE_CHOICES = (
   ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
   ("Andhra Pradesh","Andhra Pradesh"),
   ("Arunachal Pradesh","Arunachal Pradesh"),
   ("Assam","Assam"),
   ("Bihar","Bihar"),
   ("Chhattisgarh","Chhattisgarh"),
   ("Chandigarh","Chandigarh"),
   ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
   ("Daman and Diu","Daman and Diu"),
   ("Delhi","Delhi"),
   ("Goa","Goa"),
   ("Gujarat","Gujarat"),
   ("Haryana","Haryana"),
   ("Himachal Pradesh","Himachal Pradesh"),
   ("Jammu and Kashmir","Jammu and Kashmir"),
   ("Jharkhand","Jharkhand"),
   ("Karnataka","Karnataka"),
   ("Kerala","Kerala"),
   ("Ladakh","Ladakh"),
   ("Lakshadweep","Lakshadweep"),
   ("Madhya Pradesh","Madhya Pradesh"),
   ("Maharashtra","Maharashtra"),
   ("Manipur","Manipur"),
   ("Meghalaya","Meghalaya"),
   ("Mizoram","Mizoram"),
   ("Nagaland","Nagaland"),
   ("Odisha","Odisha"),
   ("Punjab","Punjab"),
   ("Pondicherry","Pondicherry"),
   ("Rajasthan","Rajasthan"),
   ("Sikkim","Sikkim"),
   ("Tamil Nadu","Tamil Nadu"),
   ("Telangana","Telangana"),
   ("Tripura","Tripura"),
   ("Uttar Pradesh","Uttar Pradesh"),
   ("Uttarakhand","Uttarakhand"),
   ("West Bengal","West Bengal")
)

EVENT = (
    ('national','national'),
    ('international','international'),
)

LEVEL = (
    ('national','national'),
    ('international','international'),
)

class SportsAchievements(models.Model):
    tournament_name = models.CharField(max_length=256,blank=True,null=True)
    venue = models.CharField(max_length=100,blank=True,null=True)
    date_from = models.DateField(blank=True,null=True)
    date_to = models.DateField(blank=True,null=True)
    achievement = models.CharField(max_length=100,blank=True,null=True)
    event_type = models.CharField(max_length=50,choices=EVENT,blank=True,null=True)
    scholar = models.ForeignKey('Scholarship',on_delete=models.CASCADE,related_name='related_ach',blank=True,null=True)

    def __str__(self):
        return self.tournament_name

class SportCertificates(models.Model):
    certificate = models.FileField(upload_to='certificates',blank=True,null=True)
    scholar = models.ForeignKey('Scholarship',on_delete=models.CASCADE,related_name='related_cert',blank=True,null=True)

    def __str__(self):
        return 'sport certificate ' + str(self.id)

class OtherDocuments(models.Model):
    photo = models.FileField(upload_to='documents/photo',blank=True,null=True)
    sign = models.FileField(upload_to='documents/sign',blank=True,null=True) 
    birth_certificate = models.FileField(upload_to='documents/birth-cert',blank=True,null=True) 
    aadhar = models.FileField(upload_to='documents/aadhar',blank=True,null=True) 
    pan = models.FileField(upload_to='documents/pan',blank=True,null=True) 
    passport = models.FileField(upload_to='documents/passport',blank=True,null=True)
    scholar = models.ForeignKey('Scholarship',on_delete=models.CASCADE,related_name='related_other',blank=True,null=True)

    def __str__(self):
        return 'other docs ' + str(self.id)

class Scholarship(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    sport = models.CharField(max_length=20,choices=SPORT,blank=True,null=True)
    playing_position = models.CharField(max_length=20,choices=POSITION,blank=True,null=True)
    category = models.CharField(max_length=20,choices=CATEGORY,blank=True,null=True)
    level = models.CharField(max_length=50,choices=LEVEL,blank=True,null=True)
    is_ews = models.BooleanField(default=False)
    gender = models.CharField(max_length=20,choices=GENDER,blank=True,null=True)
    parent_name = models.CharField(max_length=256,blank=True,null=True)
    mobile_number = models.CharField(max_length=13,blank=True,null=True)
    aadhar_number = models.CharField(max_length=20,blank=True,null=True)
    pan_number = models.CharField(max_length=10,blank=True,null=True)
    passport_number = models.CharField(max_length=10,blank=True,null=True)
    address = models.TextField(blank=True,null=True)
    district = models.CharField(max_length=100,blank=True,null=True)
    state = models.CharField(max_length=50,choices=STATE_CHOICES,blank=True,null=True)
    pin_code = models.CharField(max_length=10,null=True,blank=True)
    educational_details = models.CharField(max_length=20,blank=True,null=True)
    other_achievements = models.TextField(blank=True,null=True)
    place = models.CharField(max_length=20,blank=True,null=True)
    date = models.DateField(_("Date"), default=date.today)
    declare = models.BooleanField(default=False)
    tnc =models.BooleanField(default=False)

    class Meta:
        verbose_name = "Scholars"
        verbose_name_plural = "Scholars"
    
    def __str__(self):           
        return str(self.id)