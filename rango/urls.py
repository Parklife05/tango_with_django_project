from django.conf.urls import url
from rango import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^index/$', views.index, name='Index'),
    url (r'^about/$',views.about, name = 'About')] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

