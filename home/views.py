from django.shortcuts import render
# Create your views here.
from django.shortcuts import render

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


class AllScholarView(APIView):
    parser_classes = (MultiPartParser, FormParser, )
    def get(self, request,*args, **kwargs):
        obj = Scholarship.objects.all()
        ser = ScholarSerializers(obj,many=True)
        return Response(ser.data)
    
    def post(self, request, format=None):
        data = request.data
        main_data = data['main']
        serializer = ScholarSerializers(data=main_data)
        if serializer.is_valid():
            obj = serializer.save()
            for i in data['sports_achievements']:
                ach_obj = AchivementSerializers(data=i)
                ach_obj.scholar = obj
                ach_obj.save()
            for i in data['sports_certificates']:
                certs = dict((request.FILES).lists()).get('certificate', None)
                for c in certs:
                    cert_data = {}
                    cert_data["certificate"] = c
                    cert_obj = CertificateSerializers(data=cert_data)
                    if cert_obj.is_valid():
                        cert_obj.scholar = obj
                        serializer.save()
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
            data['achivement'] = ach_ser.data

            cert_ser = CertificateSerializers(cert_obj,many=True)
            data['certificates'] = cert_ser.data

            return Response(data, status=status.HTTP_200_OK)
        return Response(data, status=status.HTTP_200_OK)
        
