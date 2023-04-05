from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.views import View
from django.http import HttpResponse

from search_code.models import Code, Category
from .serializers import CodeSerialzier


class CodeView(APIView):
    
    queryset = Code.objects.all()
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return self.queryset.select_related('category')

    def get(self, request, code, *args, **kwargs):
        code = code.replace(' ', '')
        if len(code) == 6:
            code = f'{code[:2]}.{code[2:4]}.{code[4:]}'
        objs = self.get_queryset().filter(children__parent__code__startswith=code)
        serializer = CodeSerialzier(instance=objs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
