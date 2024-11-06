from atexit import register
from django import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import about_form_view, adoption_form_view, adoption_success_view, contact_view, home,adopt_view,resources_view,get_involved , about, success
urlpatterns = [
    path('', home, name='home'),
    path('adopt/', adopt_view, name='adopt'),  
    path('about/',about, name='about'),
    path('involved/', get_involved, name='involved'),
    path('resources/', resources_view, name='resources'),
    path('success/', success, name='success'),
    path('contact/', contact_view, name='contact'),
    path('about-form/', about_form_view, name='about_form'),
    path('adoption/', adoption_form_view, name='adoption_form'),
    path('adoptsuccess/', adoption_success_view, name='adoption_success'), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
