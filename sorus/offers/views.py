from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from offers.serializers import CreateReviewSerializer, CreateOfferSerializer


@api_view(['POST'])
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
