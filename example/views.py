from django.http import HttpResponse
from django.contrib.auth.models import User


def home(request):
  return HttpResponse(
      'Hello! The database has {} users'.format(User.objects.count()))
