from django.conf.urls import include, url
from django.contrib import admin

# urls paths
urlpatterns = [
    url(r'^BookShop/', include('BookShop.urls')),
    url(r'^', include('BookShop.urls', namespace='BookShop')),
    url(r'^admin/', admin.site.urls),
]