from django.contrib import admin
from django.urls import path

import file.urls
import user.urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('file/', file.urls),
    path('user/',user.urls)
]
