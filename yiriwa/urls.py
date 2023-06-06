from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
]


#Configure Admin_titles
admin.site.site_header = "YIRIWA"
admin.site.site_title = "YIRIWA"