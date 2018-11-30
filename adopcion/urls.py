from django.conf.urls import url
from adopcion.views import DogList
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('dogs/', DogList.as_view(), name='doglist'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
