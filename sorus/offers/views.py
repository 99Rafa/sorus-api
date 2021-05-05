from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from offers.serializers import CreateReviewSerializer


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
