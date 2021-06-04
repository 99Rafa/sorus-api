from datetime import datetime
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from status.models import State
from sales.serializers import CreateSaleSerializer


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
    pass
