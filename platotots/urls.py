from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()


urlpatterns = [

    url(r'^platoweb/', include('platoweb.urls')),
    url(r'^admin/', admin.site.urls),
# .   url(r'^posts/', include("posts.urls", namespace='posts')),
]