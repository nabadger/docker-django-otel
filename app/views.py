from __future__ import unicode_literals

from django.http import HttpResponse
from .models import string

def app(request):
    strings = string.objects.all()
    output = '<br>'.join([s.string for s in strings])
    return HttpResponse(output)
