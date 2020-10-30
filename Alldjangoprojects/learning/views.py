from django.shortcuts import render
from learning.models import Post
from learning.serializers import PostSerializer
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

@api_view(['GET'])
def welcome(request):
    return JsonResponse({"message":"welcome to our django api endpoints"})


@api_view(['GET', 'POST', 'DELETE'])
def post_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
     if request.method == 'GET':
        post = Post.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            post = post.filter(title__icontains=title)
        post_serializer = PostSerializer(post, many=True)
        return JsonResponse(post_serializer.data, safe=False)
     elif request.method == 'POST':
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    # find tutorial by pk (id)
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return JsonResponse({'message': 'The Post does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET / PUT / DELETE tutorial
    if request.method == 'GET':
        post_serializer = PostSerializer(post)
        return JsonResponse(post_serializer.data)
    elif request.method == 'PUT':
        post_data = JSONParser().parse(request)
        post_serializer = PostSerializer(post, data=post_data)
        if post_serializer.is_valid():
            post_serializer.save()
            return JsonResponse(post_serializer.data)
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return JsonResponse({'message': 'Post was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        count = Post.objects.all().delete()
        return JsonResponse({'message': '{} Posts were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def post_list_published(request):
    # GET all published tutorials
    post = Post.objects.filter(published=True)
    if request.method == 'GET':
        post_serializer = PostSerializer(post, many=True)
        return JsonResponse(post_serializer.data, safe=False)
