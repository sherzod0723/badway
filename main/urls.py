from django.urls import path
from .views import *
from django.conf.urls import handler404


handler404 = custom_404_view

urlpatterns = [
    path('secure-word/<int:pk>/download-pdf/', access_code_view, name='download_pdf_view'),
    path('ru/file/download/', access_code_view, name='secure_word_login'),
    path('ru/file/download/<int:code>/', access_code_view, name='secure_word_login'),
    path('', base_redirect, name='base_redirect'),
]


