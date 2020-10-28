from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('muffinShop/', include('muffinShop.urls')),
    path('admin/', admin.site.urls),

]