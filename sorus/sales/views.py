from datetime import datetime
from uuid import uuid4

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from status.models import State
from users.models import User
from offers.models import Product
from sales.models import Sale
from sales.serializers import (
    CreateSaleSerializer,
    UpdateUserSubscriptionSerializer,
    ListUserBuysSerializer
)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def buy_product(request):
    req_data = request.data
    sale_data = {
        'product': req_data['product'],
        'buyer': req_data['user'],
        'price': req_data['total'],
        'quantity': 1,
        'buy_method': 1,
        'buy_date': datetime.now(),
        'reference': str(uuid4())
    }
    serializer = CreateSaleSerializer(data=sale_data)
    if serializer.is_valid():
        product = serializer.validated_data['product']
        product.stock -= 1
        if product.stock <= 0:
            product.state = State.objects.get(id=2)
        product.save()
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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def buy_subscription(request):
    sub = {'subscription': 2}
    user = User.objects.get(id=request.data['user'])
    serializer = UpdateUserSubscriptionSerializer(user, data=sub, partial=True)

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


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_buys(request):
    sale = Sale.objects.filter(buyer=request.user.id)
    serializer = ListUserBuysSerializer(sale, many=True)
    return Response(
        data=serializer.data,
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_sales(request):
    sales = Sale.objects.filter(product__promoter=request.user.id)
    serializer = ListUserBuysSerializer(sales, many=True)
    return Response(
        data=serializer.data,
        status=status.HTTP_200_OK
    )
