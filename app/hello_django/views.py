from rest_framework import  viewsets
from django.http import HttpResponse
from django.db import connection
import django


from .serializers import UserSerializer, RoomSerializer, MessageSerializer
from .models import User, Room, Messages

def student_show(request):
    # something = User
    # print(something)
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM django_migrations''')

    print('====================================>')
    print("DB information", cursor.fetchone())
    print('====================================')
    x = []
    for i in range(10):
        x.append(i)

    django_version = django.VERSION
    print(django_version)
    test_response = "<h1>DataFlair Django </h1>The Digits updated are {0}".format(x) + "django version =>" + ''
    return HttpResponse(test_response)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer


