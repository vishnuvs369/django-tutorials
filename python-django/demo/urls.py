
from django.contrib import admin
from django.urls.conf import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
]

