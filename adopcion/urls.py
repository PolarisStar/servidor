from django.conf.urls import url
from adopcion.views import DogList
from django.urls import path
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.conf import settings
from . import views
from django.contrib import admin
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'Dog', views.viewsets.GenericViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dogs/', DogList.as_view(), name='doglist'),
    url(r'^', include(router.urls) ),
    url(r'âpi-auth/', include ('rest_framework.urls' , namespace="rest_framework"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
