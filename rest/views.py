from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from users.models import User
from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import pycassa
from django.conf import settings
from rest.forms import UserGetListForm
from users.util import BadRequestException


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class UsersListView(APIView):
    '''
       Used for searching by properties or listing all users available.
    '''
    def get(self, request):
        # get the offset and limit query parameters
        form = UserGetListForm(request.QUERY_PARAMS)
        
        if form.is_valid():
            return Response(UserSerializer(form.submit(), many=True))
        else:
            raise BadRequestException()
            

    '''

    
    def post(self, request):
        pass
    '''   