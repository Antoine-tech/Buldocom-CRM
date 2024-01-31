from django.contrib import admin
from django.urls import path, include

import website

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
]
