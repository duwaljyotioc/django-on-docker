from rest_framework import mixins
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import django

from app.hello_django.models import User
from app.hello_django.serializers import UserSerializer


# from app.hello_django.models import User
# from app.hello_django.serializers import UserSerializer


# from app.hello_django.models import User

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


class UserViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer


