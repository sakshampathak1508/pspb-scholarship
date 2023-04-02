from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
import json
# Create your views here.
from . models import SportsAchievements,Scholarship,SportCertificates
from . serializers import (
    ScholarSerializers,AchivementSerializers,CertificateSerializers
)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import pagination,generics


# test_data = {
#     "main_data": {
#         "name": "virat kohli",
#         "sport": "cricket",
#         "playing_position": "winner",
#         "category": "senior",
#         "level": "national",
#         "is_ews": True,
#         "gender": "male",
#         "parent_name": "Mr Kohli",
#         "mobile_number": 9818182074,
#         "aadhar_number": 274714716693,
#         "pan_number": "GMUPP4936T",
#         "address": "221 B Baker Street",
#         "district": "Palam Vihar",
#         "state": "Haryana",
#         "pin_code": 122017,
#         "educational_details": "BA PASS",
#         "other_achievements": "Winner of IPL",
#         "photo": "/media/documents/photo/licha.pdf",
#         "sign": "/media/documents/sign/licha.pdf",
#         "birth_certificate": "/media/documents/birth-cert/licha.pdf",
#         "aadhar": "/media/documents/aadhar/licha.pdf",
#         "pan": "/media/documents/pan/licha.pdf",
#         "passport": "/media/documents/passport/licha.pdf",
#         "place": "New Delhi",
#         "date": "2023-03-28"
#     },
#     "achivements": [
#         {
#             "tournament_name": "World cup",
#             "venue": "Austraila",
#             "date_from": "2022-03-28",
#             "date_to": "2022-04-28",
#             "achievement": "Winner",
#             "event_type": "international",
#         },
#         {
#             "tournament_name": "IPL",
#             "venue": "India",
#             "date_from": "2023-03-28",
#             "date_to": "2023-04-28",
#             "achievement": "Winner",
#             "event_type": "national",
#         }
#     ],
#     "certificates" : []
# }

# "certificates": [
    #     {
    #         "id": 1,
    #         "certificate": "/media/certificates/licha.pdf",
    #         "scholar": 1
    #     },
    #     {
    #         "id": 2,
    #         "certificate": "/media/certificates/licha_TxmBC7o.pdf",
    #         "scholar": 1
    #     }
    # ]



class AllScholarView(APIView):
    # parser_classes = (MultiPartParser, FormParser,)
    def get(self, request,*args, **kwargs):
        obj = Scholarship.objects.all()
        ser = ScholarSerializers(obj,many=True)
        return Response(ser.data)
    
    def post(self, request):
        print(request.data)
        main_data = request.data['main_data']
        ach = request.data['achivements']
        cert = request.data['certificates']
        print(main_data)
        print(ach)
        print(cert)
        serializer = ScholarSerializers(data=main_data)
        if serializer.is_valid():
            obj = serializer.save()
            for i in ach:
                i['scholar'] = obj.id
                ach_obj = AchivementSerializers(data=i)
                if ach_obj.is_valid():
                    ach_obj.save()
            for i in cert:
                certs = dict((request.FILES).lists()).get('certificate', None)
                for c in certs:
                    cert_data = {}
                    cert_data["certificate"] = c
                    cert_data['scholar'] = obj.id
                    cert_obj = CertificateSerializers(data=cert_data)
                    if cert_obj.is_valid():
                        cert_obj.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AllDataTabularFormView(APIView):
     def get(self, request, *args, **kwargs):
        data = {}
        sid = request.GET.get('id','')
        obj = Scholarship.objects.filter(id=sid).first()
        if obj:
            ach_obj = SportsAchievements.objects.filter(scholar=obj)
            cert_obj = SportCertificates.objects.filter(scholar=obj)
            
            obj_ser = ScholarSerializers(obj)
            data['main_data'] = obj_ser.data

            ach_ser = AchivementSerializers(ach_obj,many=True)
            data['achivements'] = ach_ser.data

            cert_ser = CertificateSerializers(cert_obj,many=True)
            data['certificates'] = cert_ser.data

            return Response(data, status=status.HTTP_200_OK)
        return Response(data, status=status.HTTP_200_OK)
        
