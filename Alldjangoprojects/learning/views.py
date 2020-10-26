from django.shortcuts import render




from learning.models import Post
from learning.serializers import PostSerializer
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials


@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    # find tutorial by pk (id)
    try:
        tutorial = Tutorial.objects.get(pk=pk)
    except Tutorial.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET / PUT / DELETE tutorial


@api_view(['GET'])
def tutorial_list_published(request):
    # GET all published tutorials
