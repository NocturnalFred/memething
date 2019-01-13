from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from PIL import Image

from .models import meme

def index(request) :

    image = Image.open(request.FILES['meme'])
    text = meme.getText(image)


    return HttpResponse(text)

