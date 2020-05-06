from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
# from django.conf.urls import url, include

from . import views

app_name ="main"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    # url(r'^signup/$', views.signup, name="signup"),
    # url(r'^logout/$', views.logout_request, name="logout"),
    # url(r'^login/$', views.login_request, name="login"),
    # url(r'<single_slug>', views.single_slug, name="single_slug"),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, 
                    document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, 
                    document_root=settings.MEDIA_ROOT)

