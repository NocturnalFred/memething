from django.contrib import admin
from django.urls import include, path

urlpatterns = [
        path('meme/', include('meme.urls')),
        path('admin/', admin.site.urls),
]
