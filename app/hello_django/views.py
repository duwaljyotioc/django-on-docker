from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
import django

def student_show(request):
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
