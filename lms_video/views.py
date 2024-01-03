from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Categories, SubCategory, ClassesRank, Subjects, Authors, Video, Subscribe, SubscriptionRequest
from .serializers import CategoriesSerializer, ClassesRankSerializer, SubjectsSerializer, AuthorsSerializer, \
    VideoSerializer, SubscribeSerializer, SubscriptionRequestSerializer, SubCategorySerializer
from drf_spectacular.utils import extend_schema


# Categories API views

@extend_schema(request=CategoriesSerializer)
@api_view(['GET', 'POST'])
def categories_list(request):
    if request.method == 'GET':
        categories = Categories.objects.all()
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ClassesRank API views
@extend_schema(request=ClassesRankSerializer)
@api_view(['GET', 'POST'])
def classes_rank_list(request):
    if request.method == 'GET':
        classes_rank = ClassesRank.objects.all()
        serializer = ClassesRankSerializer(classes_rank, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClassesRankSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Subjects API views
@extend_schema(request=SubjectsSerializer)
@api_view(['GET', 'POST'])
def subjects_list(request):
    if request.method == 'GET':
        subjects = Subjects.objects.all()
        serializer = SubjectsSerializer(subjects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Authors API views
@extend_schema(request=AuthorsSerializer)
@api_view(['GET', 'POST'])
def authors_list(request):
    if request.method == 'GET':
        authors = Authors.objects.all()
        serializer = AuthorsSerializer(authors, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AuthorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Video API views
@extend_schema(request=VideoSerializer)
@api_view(['GET', 'POST'])
def video_list(request):
    if request.method == 'GET':
        videos = Video.objects.all()
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=VideoSerializer)
@api_view(['GET', 'PUT', 'DELETE'])
def video_detail(request, pk):
    try:
        video = Video.objects.get(pk=pk)
    except Video.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VideoSerializer(video)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VideoSerializer(video, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Subscribe API views
@extend_schema(request=SubscribeSerializer)
@api_view(['GET', 'POST'])
def subscribe_list(request):
    if request.method == 'GET':
        subscriptions = Subscribe.objects.all()
        serializer = SubscribeSerializer(subscriptions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubscribeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=SubscriptionRequestSerializer)
@api_view(['GET', 'POST'])
def create_subscription_request(request):
    if request.method == 'GET':
        subscription_requests = SubscriptionRequest.objects.all()
        serializer = SubscriptionRequestSerializer(subscription_requests, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubscriptionRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_subcategories(request):
    if request.method == 'GET':
        subcategories = SubCategory.objects.all()
        serializer = SubCategorySerializer(subcategories, many=True)
        return Response(serializer.data)
