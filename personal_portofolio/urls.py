"""personal_portofolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from django.conf.urls.static import static
from django.conf import settings
from portofolio import views

admin.site.site_header = "Portfolio Admin"
admin.site.site_title = "Administration Portal"
admin.site.index_title = "Welcome my League!"


urlpatterns = [
    path('', views.HomePage, name = "home"),
    path('detail/',views.detail,name='detail'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('interactive_dictionary/',include('interactive_dictionary.urls')),
    path('todos/',include('todos.urls')),
    path('bookAnalyzer/',include('bookAnalyzer.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
