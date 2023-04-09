from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
import json
# Create your views here.
from . models import OtherDocuments,SportsAchievements,Scholarship,SportCertificates
from . serializers import (
    ScholarSerializers,AchivementSerializers,CertificateSerializers,OtherDocumentsSerializers
)
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import pagination,generics


class AllScholarView(APIView):
    def get(self, request,*args, **kwargs):
        obj = Scholarship.objects.all()
        ser = ScholarSerializers(obj,many=True)
        return Response(ser.data)
    
    def post(self, request):
        print(request.data)
        main_data = request.data['main_data']
        ach = request.data['achivements']
        print(main_data)
        print(ach)
        serializer = ScholarSerializers(data=main_data)
        if serializer.is_valid():
            obj = serializer.save()
            for i in ach:
                i['scholar'] = obj.id
                ach_obj = AchivementSerializers(data=i)
                if ach_obj.is_valid():
                    ach_obj.save()
            return Response({"scholar" : serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class UploadDocsView(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    def post(self,request):
        print(request.data)
        docs = OtherDocumentsSerializers(data=request.data)
        if docs.is_valid():
            docs.save()
            return Response({"status" : "docs created"}, status=status.HTTP_201_CREATED)
        return Response(docs.errors, status=status.HTTP_400_BAD_REQUEST)

class CertificateView(APIView):
    parser_classes = (MultiPartParser, FormParser,)
    def post(self,request):
        print(request.data)
        sid = request.GET.get('sid',None)
        if request.FILES:
            certs = dict((request.FILES).lists()).get('files', None)
            if certs:
                for c in certs:
                    cert_data = {}
                    cert_data["certificate"] = c
                    cert_data["scholar"] = sid 
                    serializer = CertificateSerializers(data=cert_data)
                    if serializer.is_valid():
                        serializer.save()
            return Response({"status" : "certificates created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AllDataTabularFormView(APIView):
     def get(self, request, *args, **kwargs):
        data = {}
        sid = request.GET.get('id','')
        obj = Scholarship.objects.filter(id=sid).first()
        if obj:
            ach_obj = SportsAchievements.objects.filter(scholar=obj)
            cert_obj = SportCertificates.objects.filter(scholar=obj)
            other_docs_obj = OtherDocuments.objects.filter(scholar=obj)

            
            obj_ser = ScholarSerializers(obj)
            data['main_data'] = obj_ser.data

            other_docs = OtherDocumentsSerializers(other_docs_obj,many=True)
            data['other_docs'] = other_docs.data

            ach_ser = AchivementSerializers(ach_obj,many=True)
            data['achivements'] = ach_ser.data

            cert_ser = CertificateSerializers(cert_obj,many=True)
            data['certificates'] = cert_ser.data

            return Response(data, status=status.HTTP_200_OK)
        return Response(data, status=status.HTTP_200_OK)