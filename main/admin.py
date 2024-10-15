from django.contrib import admin
from django.http import HttpResponse, Http404
from django.utils.html import format_html
from .models import *
import os
from django.shortcuts import get_object_or_404
from django.urls import reverse

#
# class SecureWordAdmin(admin.ModelAdmin):
#     list_display = ('access_code', 'download_continue_word')
#
#     def download_continue_word(self, obj):
#         if obj.continue_word:
#             return format_html('<a href="{}">Download</a>', obj.get_download_url())
#         return "No file available"
#     download_continue_word.allow_tags = True
#     download_continue_word.short_description = "Download Continue Word"
#
#     def get_urls(self):
#         from django.urls import path
#         urls = super().get_urls()
#         custom_urls = [
#             path('<int:secureword_id>/download/', self.admin_site.admin_view(self.download_file), name='secureword_download'),
#         ]
#         return custom_urls + urls
#
#     def download_file(self, request, secureword_id):
#         obj = self.get_object(request, secureword_id)
#         if not obj or not obj.continue_word:
#             raise Http404("No file found.")
#
#         file_path = obj.continue_word.path
#         if os.path.exists(file_path):
#             with open(file_path, 'rb') as file:
#                 response = HttpResponse(file.read(), content_type="application/pdf")
#                 response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
#                 return response
#         raise Http404("File not found.")
#
# admin.site.register(SecureWord, SecureWordAdmin)
#
# class SecureWordAdmin2(admin.ModelAdmin):
#     list_display = ('access_code', 'download_continue_word')
#
#     def download_continue_word(self, obj):
#         if obj.continue_word:
#             return format_html('<a href="{}">Download</a>', obj.get_download_url())
#         return "No file available"
#     download_continue_word.allow_tags = True
#     download_continue_word.short_description = "Download Continue Word"
#
#     def get_urls(self):
#         from django.urls import path
#         urls = super().get_urls()
#         custom_urls = [
#             path('<int:secureword2_id>/download/', self.admin_site.admin_view(self.download_file), name='secureword2_download'),
#         ]
#         return custom_urls + urls
#
#     def download_file(self, request, secureword2_id):
#         obj = self.get_object(request, secureword2_id)
#         if not obj or not obj.continue_word:
#             raise Http404("No file found.")
#
#         file_path = obj.continue_word.path
#         if os.path.exists(file_path):
#             with open(file_path, 'rb') as file:
#                 response = HttpResponse(file.read(), content_type="application/pdf")
#                 response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
#                 return response
#         raise Http404("File not found.")
#
# admin.site.register(SecureWord2, SecureWordAdmin2)
#
# class SecureWordAdmin3(admin.ModelAdmin):
#     list_display = ('access_code', 'download_continue_word')
#
#     def download_continue_word(self, obj):
#         if obj.continue_word:
#             return format_html('<a href="{}">Download</a>', obj.get_download_url())
#         return "No file available"
#     download_continue_word.allow_tags = True
#     download_continue_word.short_description = "Download Continue Word"
#
#     def get_urls(self):
#         from django.urls import path
#         urls = super().get_urls()
#         custom_urls = [
#             path('<int:secureword3_id>/download/', self.admin_site.admin_view(self.download_file), name='secureword3_download'),
#         ]
#         return custom_urls + urls
#
#     def download_file(self, request, secureword3_id):
#         obj = self.get_object(request, secureword3_id)
#         if not obj or not obj.continue_word:
#             raise Http404("No file found.")
#
#         file_path = obj.continue_word.path
#         if os.path.exists(file_path):
#             with open(file_path, 'rb') as file:
#                 response = HttpResponse(file.read(), content_type="application/pdf")
#                 response['Content-Disposition'] = f'attachment; filename={os.path.basename(file_path)}'
#                 return response
#         raise Http404("File not found.")
#
# admin.site.register(SecureWord3, SecureWordAdmin3)

from django.http import FileResponse
from django.utils.html import format_html
from django.urls import path

class SecurityPdfAdmin(admin.ModelAdmin):
    list_display = ('continue_word', 'clickable_access_code', 'download_pdf_button','link')

    # Custom download button in the list view
    def download_pdf_button(self, obj):
        # Check if the file exists and if it is a PDF
        if obj.continue_word and obj.continue_word.name.endswith('.pdf'):
            return format_html('<a class="button" href="{}">Download PDF</a>', f'./download_pdf/{obj.id}')
        return "No PDF available"

    download_pdf_button.short_description = "Download PDF"

    # Define custom admin URL for downloading the PDF
    def clickable_access_code(self, obj):
        # Generate the admin URL for editing the object
        url = reverse('admin:main_security_pdf_change', args=[obj.id])
        return format_html('<a href="{}">{}</a>', url, obj.access_code)

    clickable_access_code.short_description = "Access Code"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('download_pdf/<int:pk>/', self.download_pdf, name='download_pdf'),
        ]
        return custom_urls + urls

    # Custom download view
    def download_pdf(self, request, pk):
        obj = get_object_or_404(Security_pdf, pk=pk)
        if obj.continue_word and obj.continue_word.name.endswith('.pdf'):
            # Serve the PDF file for download
            return FileResponse(open(obj.continue_word.path, 'rb'), as_attachment=True, filename=obj.continue_word.name)
        return HttpResponse('PDF not found or invalid file type.')


admin.site.register(Security_pdf, SecurityPdfAdmin)



