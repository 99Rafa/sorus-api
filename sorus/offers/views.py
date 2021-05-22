from django.db.models import Q
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from offers.models import Product
from offers.pagination import OffersPagination
from offers.serializers import (
    CreateReviewSerializer,
    CreateOfferSerializer,
    ListOfferSerializer,
    UpdateOfferSerializer
)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_review(request):
    serializer = CreateReviewSerializer(data=request.data)
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
def create_offer(request):
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
    paginator = OffersPagination()
    paginator.page_size = 15
    products = Product.objects.all().order_by('start_date')
    result_page = paginator.paginate_queryset(products, request)
    serializer = ListOfferSerializer(result_page, many=True)
    data = [p for p in serializer.data if p['still_active']]
    return paginator.get_paginated_response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def search_offers(request):
    paginator = OffersPagination()
    paginator.page_size = 15
    query = request.data
    products = Product.objects.filter(
        Q(state=1),
        Q(name__icontains=query) | Q(description__icontains=query)
    ).order_by('start_date')
    result_page = paginator.paginate_queryset(products, request)
    serializer = ListOfferSerializer(result_page, many=True)
    data = [p for p in serializer.data if p['still_active']]
    return paginator.get_paginated_response(data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_user_offers(request):
    products = Product.objects.filter(promoter=request.user)
    serializer = ListOfferSerializer(products, many=True)
    return Response(
        data=serializer.data,
        status=status.HTTP_200_OK
    )


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_product(request):
    product = Product.objects.get(id=request.data['id'])
    if request.user == product.promoter:
        serializer = UpdateOfferSerializer(product, data=request.data, partial=True)
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
