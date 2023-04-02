from rest_framework import serializers
from .models import SportsAchievements,Scholarship,SportCertificates,OtherDocuments

class ScholarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Scholarship
        fields = '__all__'

class AchivementSerializers(serializers.ModelSerializer):
    class Meta:
        model = SportsAchievements
        fields = '__all__'

class CertificateSerializers(serializers.ModelSerializer):
    class Meta:
        model = SportCertificates
        fields = '__all__'
    
class OtherDocumentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = OtherDocuments
        fields = '__all__'