# -*- coding:utf-8 -*-
# !/usr/bin/env python
# Time 18-3-19
# Author Yo
# Email YoLoveLife@outlook.com
from yocdn import models,serializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response, status
from django.conf import settings
from rest_framework import generics
from deveops.api import WebTokenAuthentication
__all__ = [

]


class YoCDNPagination(PageNumberPagination):
    page_size = 10


class YoCDNListByPageAPI(WebTokenAuthentication, generics.ListAPIView):
    module = models.CDN
    serializer_class = serializers.YoCDNSerializer
    queryset = models.CDN.objects.all()
    permission_classes = [AllowAny,]
    pagination_class = YoCDNPagination


class YoCDNCreateAPI(WebTokenAuthentication, generics.CreateAPIView):
    module = models.CDN
    serializer_class = serializers.YoCDNListSerializer
    permission_classes = [AllowAny,]