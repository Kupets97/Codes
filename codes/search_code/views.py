from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


from search_code.models import Code
from .serializers import CodeSerialzier


class CodeView(APIView):
    
    queryset = Code.objects.all()
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return self.queryset.select_related('category')

    def get(self, request, code, *args, **kwargs):
        code = code.replace(' ', '').replace('.', '') 
        objs = self.get_queryset().filter(children__parent__clean_code__startswith=code)
        serializer = CodeSerialzier(instance=objs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
