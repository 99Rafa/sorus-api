from random import randint

from django.db.models import Q
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from offers.models import Product, Category, Review
from offers.pagination import OffersPagination
from offers.serializers import (
    CreateReviewSerializer,
    CreateOfferSerializer,
    ListOfferSerializer,
    UpdateOfferSerializer,
    ListCategoriesSerializer,
    ListReviewsSerializer
)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request):
    data = {
        **request.data,
        'user': request.user.id
    }
    serializer = CreateReviewSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            data={'message': 'Success'},
            status=status.HTTP_201_CREATED
        )
    else:
        return Response(
            data={'message': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def list_comments(request):
    reviews = Review.objects.filter(product=request.data['product']).order_by('-date')
    serializer = ListReviewsSerializer(reviews, many=True)
    return Response(
        data=serializer.data,
        status=status.HTTP_200_OK
    )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_offer(request):
    if request.user.subscription.id == 1 and Product.objects.filter(promoter=request.user.id, state=1).count() >= 5:
        return Response(
            data={'message': 'error'},
            status=status.HTTP_400_BAD_REQUEST
        )
    data = {
        **request.data,
        'promoter': request.user.pk,
        'state': '1'
    }
    serializer = CreateOfferSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            data={'message': 'success'},
            status=status.HTTP_201_CREATED
        )
    else:
        return Response(
            data={'message': 'error'},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_offers(request):
    args = request.GET
    paginator = OffersPagination()
    paginator.page_size = 15
    products = Product.objects.filter(state=1, end_date__gt=timezone.now()).order_by('start_date')

    if 'category' in args:
        products = products.filter(category=args['category'])
    if 'query' in args:
        products = products.filter(
            Q(name__icontains=args['query']) | Q(description__icontains=args['query'])
        )
    if 'hot' in args:
        products = products.order_by('promoter__stars')

    result_page = paginator.paginate_queryset(products, request)
    serializer = ListOfferSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_user_offers(request):
    products = Product.objects.filter(promoter=request.user, state=1)
    serializer = ListOfferSerializer(products, many=True)
    return Response(
        data=serializer.data,
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_top_offers(request):
    offers = Product.objects.filter(promoter__subscription=2, state=1, end_date__gt=timezone.now())
    total = len(offers)
    if total == 0:
        return Response(
            data=[],
            status=status.HTTP_200_OK
        )
    elif 1 <= total <= 2:
        top_offers = offers
    else:
        top_offers = [
            offers[randint(0, int(total / 2))],
            offers[randint(int(total / 2) + 1, total - 1)]
        ]
    serializer = ListOfferSerializer(top_offers, many=True)
    return Response(
        data=serializer.data,
        status=status.HTTP_200_OK
    )


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_product(request):
    product = Product.objects.get(id=request.data['id'])
    if request.user == product.promoter:
        serializer = UpdateOfferSerializer(
            product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={'message': 'success'},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    else:
        return Response(
            data={'message': "You don't own this product"},
            status=status.HTTP_403_FORBIDDEN
        )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_categories(request):
    categories = Category.objects.all()
    serializer = ListCategoriesSerializer(categories, many=True)
    return Response(
        data=serializer.data,
        status=status.HTTP_200_OK
    )
