from rest_framework import serializers
from .models import SportsAchievements,Scholarship,SportCertificates

# class ScholarSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Scholarship
#         fields = ('id',
#                 'name',
#                 'sport',
#                 'playing_position',
#                 'category',
#                 'is_ews',
#                 'gender',
#                 'parent_name',
#                 'mobile_number',
#                 'aadhar_number',
#                 'pan_number',
#                 'passport_number',
#                 'address',
#                 'district',
#                 'state',
#                 'pin_code',
#                 'educational_details',
#                 'photo',
#                 'sign',
#                 'birth_certificate',
#                 'aadhar',
#                 'pan',
#                 'passport',
#                 'place',
#                 'date',
# )

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