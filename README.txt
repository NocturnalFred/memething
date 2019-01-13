This is a webserver that uses tesseract's OCR abilities to read text from images.

In order to use it you just need to make a request and supply a File with the key meme.

EG: curl -F "meme=@/path/to/image.jpg" http://127.0.0.1:8000/meme/ 

Installation Guide:

Install Tesseract https://github.com/tesseract-ocr/tesseract
Install pysseract https://pypi.org/project/pytesseract/

Pysseract requires the Image import from PIL or Pillow so you must install one of them.
https://pillow.readthedocs.io/en/stable/

Optionally you may install a database such as mysql or apache.  see Django documentation for more information.  https://www.djangoproject.com/



