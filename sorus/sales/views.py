from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from status.models import State
from users.models import User
from sales.serializers import (
    CreateSaleSerializer,
    UpdateUserSubscriptionSerializer
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
        'buy_date': datetime.now()
    }
    serializer = CreateSaleSerializer(data=sale_data)
    if serializer.is_valid():
        product = serializer.validated_data['product']
        product.state = State.objects.get(id=2)
        product.save()
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
