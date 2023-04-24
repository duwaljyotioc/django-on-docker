from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

def student_show(request):
    cursor = connection.cursor()
    cursor.execute('''SELECT * FROM django_migrations''')
    print(cursor.fetchone())
    x = []
    for i in range(10):
        x.append(i)
    return HttpResponse("<h1>DataFlair Django Tutorials</h1>The Digits are {0}".format(x))
