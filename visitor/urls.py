from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.urls import path, include
from visitor import views


urlpatterns = [
    url(r'', views.homepage, name="homepage")  # 首页

    # path('admin/', admin.site.urls),
]
