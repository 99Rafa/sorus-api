from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import requests

from users.models import User


class Login(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            data={
                'token': token.key,
                'user_id': user.pk,
                'user_type_id': user.user_type.pk,
            },
            status=status.HTTP_200_OK
        )


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    request.user.auth_token.delete()
    return Response(
        data={'message': 'success'},
        status=status.HTTP_200_OK
    )

  
@api_view(['POST'])
def send_notification_user(request):
    user = User.objects.get(id=request.data['id'])
    token_user = user.notification_token
    response_expo = send_notification_expo_user(token_user, request)
    if 'errors' in response_expo.keys():
        return Response(
            data={'message': 'Error'},
            status=status.HTTP_400_BAD_REQUEST
        )
    else:
        return Response(
            data={'message': 'Success'},
            status=status.HTTP_200_OK
        )


@api_view(['POST'])
def send_notification(request):
    user = User.objects.all()
    token_list = []
    for token in user:
        token_list.append(token.notification_token)
    response_expo = send_notification_expo(token_list, request)
    if 'errors' in response_expo.keys():
        return Response(
            data={'message': 'Error'},
            status=status.HTTP_400_BAD_REQUEST
        )
    else:
        return Response(
            data={'message': 'Success'},
            status=status.HTTP_200_OK
        )


def send_notification_expo(token_list, request):
    response = requests.post(
        url='https://exp.host/--/api/v2/push/send',
        json={
            'to': token_list,
            'title': request.data['title'],
            'body': request.data['body']
        }
    )
    res = response.json()
    return res


def send_notification_expo_user(token_user, request):
    response = requests.post(
        url='https://exp.host/--/api/v2/push/send',
        json={
            'to': token_user,
            'title': request.data['title'],
            'body': request.data['body']
        }
    )
    res = response.json()
    return res
