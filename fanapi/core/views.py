from django.shortcuts import render
from django.shortcuts import render_to_response
from core.models  import *


def home(request):

    m = Map(name="Test")

    m.generate(100, 100)

    return render_to_response('home.html', {"map": m, "rap": 34})

