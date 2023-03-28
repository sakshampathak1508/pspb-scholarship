from django.contrib import admin
from . models import Scholarship,SportCertificates,SportsAchievements
# Register your models here.
# class Scholarshipadmin(admin.ModelAdmin):
#     list_display = ["related_ach","related_cert","name"] 

# admin.site.register(Scholarship, Scholarshipadmin)
class SportsAchievementsInline(admin.StackedInline):
    model = SportsAchievements

class SportCertificatesInline(admin.StackedInline):
    model = SportCertificates

class ScholarshipAdmin(admin.ModelAdmin):
    inlines = [SportsAchievementsInline,SportCertificatesInline]

admin.site.register(SportCertificates)
admin.site.register(SportsAchievements)
admin.site.register(Scholarship,ScholarshipAdmin)
