from django.contrib import admin
from . models import Scholarship,SportCertificates,SportsAchievements
from django.utils.html import format_html

class SportsAchievementsInline(admin.TabularInline):
    model = SportsAchievements

class SportCertificatesInline(admin.TabularInline):
    model = SportCertificates

class ScholarshipAdmin(admin.ModelAdmin):
    inlines = [SportsAchievementsInline,SportCertificatesInline]
    list_display = ('name','sport' ,'category','gender','state','playing_position','view','download')
    search_fields = ('name','sport' ,'category','gender','state','playing_position')
    # list_editable = ('name','sport' ,'category','gender','state','playing_position')
    ordering = ('-date',)
    list_per_page = 25
    list_filter = ('name','sport' ,'category','gender','state','playing_position')
    def view(self,obj):
        return format_html(f'<a href="#" class="default">View Data</a>')
    def download(self,obj):
        return format_html(f'<a href="#" class="default">Download PDF</a>')


admin.site.register(Scholarship,ScholarshipAdmin)

@admin.register(SportsAchievements)
class SaAdmin(admin.ModelAdmin):
    list_display = ('scholar','tournament_name' ,'venue','date_from','date_to','achievement','event_type',)
    search_fields = ('scholar','tournament_name' ,'venue','date_from','date_to','event_type')
    # list_editable = ('name','sport' ,'category','gender','state','playing_position')
    ordering = ('-scholar',)
    list_per_page = 25
    list_filter = ('scholar','tournament_name' ,'venue','date_from','date_to','event_type')

@admin.register(SportCertificates)
class ScAdmin(admin.ModelAdmin):
    list_display = ('scholar','certificate')
    search_fields = ('scholar',)
    # list_editable = ('name','sport' ,'category','gender','state','playing_position')
    ordering = ('-scholar',)
    list_per_page = 25
    list_filter = ('scholar',)