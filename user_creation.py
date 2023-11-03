import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "formulario.settings")
import django
django.setup()

from django.contrib.auth.models import User


with open('users.txt', 'r') as f:
    users = f.read().splitlines()
    for i in users:
        user = i.split(' ')
        username = user[0]
        password = user[1]
        user = User.objects.create_user(username=username, password=password)
        user.save()