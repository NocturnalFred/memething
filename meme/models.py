from django.db import models
import pytesseract
# Create your models here.

class meme(models.Model) :
    image = models.ImageField()
    text = models.TextField
    text_scramble = models.TextField()


    def getText(image):
        return pytesseract.image_to_string(image)
