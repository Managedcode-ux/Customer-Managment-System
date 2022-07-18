from django.shortcuts import render
from rest_framework.views import APIView
from . models import customer
from rest_framework.response import Response
from .serializer import *


class customerView(APIView):
    serializers_class = customerSerializer

    def get(self, request, *args, **kwargs):
        detail = [{"name": detail.First_Name, "detail": detail.email}
                  for detail in customer.objects.all()]
        return Response(detail)
