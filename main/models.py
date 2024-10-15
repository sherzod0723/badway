
from django.db import models

#
# class SecureWord(models.Model):
#     word_file = models.FileField(upload_to='pdf/')
#     access_code = models.CharField(max_length=4, unique=True, blank=True)
#     qr_code = models.ImageField(upload_to='qrcodes/', blank=True)
#     continue_word = models.FileField(upload_to='docs/', blank=True)
#
#     def save(self, *args, **kwargs):
#         # Save the instance first to ensure the file is saved
#         if not self.pk:  # Check if it's a new instance
#             super(SecureWord, self).save(*args, **kwargs)
#
#         # Now that the file is saved, check if it exists
#         if not os.path.exists(self.word_file.path):
#             raise FileNotFoundError(f"The file {self.word_file.path} does not exist.")
#
#         if not self.access_code:
#             self.access_code = self.generate_unique_code()
#
#         if not self.qr_code:
#             self.generate_qr_code()
#
#         pdfmetrics.registerFont(TTFont('DejaVuSerifCondensed', 'static/ttf/DejaVuSerifCondensed.ttf'))
#         # Embed the QR code and access code into the PDF
#         self.embed_qr_code_and_access_code()
#
#         # Save the changes to the model
#         super(SecureWord, self).save(*args, **kwargs)
#
#     def generate_unique_code(self):
#         """Generate a unique 4-digit access code."""
#         while True:
#             code = get_random_string(4, allowed_chars='0123456789')
#             if not SecureWord.objects.filter(access_code=code).exists():
#                 return code
#
#     def generate_qr_code(self):
#         """Generate the QR code."""
#         qr = qrcode.QRCode(
#             version=2,
#             error_correction=qrcode.constants.ERROR_CORRECT_L,
#             box_size=10,
#             border=4,
#         )
#         qr_data = f"https://my.govuz.org/secure-word/login/{self.access_code}/"
#         qr.add_data(qr_data)
#         qr.make(fit=True)
#
#         img = qr.make_image(fill='black', back_color='white')
#         buffer = BytesIO()
#         img.save(buffer, format="PNG")
#         self.qr_code.save(f'{self.access_code}.png', File(buffer), save=False)
#
#     def embed_qr_code_and_access_code(self):
#         """Embed the QR code and access code only on the second page of the PDF."""
#         existing_pdf = PdfReader(self.word_file.path)
#         output_pdf = PdfWriter()
#
#         # Create a single overlay page with the QR code and access code
#         packet = BytesIO()
#         can = canvas.Canvas(packet, pagesize=letter)
#
#         # Draw the QR code and access code on the overlay page
#         can.drawImage(self.qr_code.path, x=457, y=612, width=95, height=95)  # Adjust coordinates as needed
#         can.setFont("DejaVuSerifCondensed", 22.5)
#         can.drawString(412, 650, f'{self.access_code}')  # Adjust coordinates as needed
#
#         can.save()
#
#         # Move to the beginning of the BytesIO buffer
#         packet.seek(0)
#
#         # Read the overlay page
#         overlay_pdf = PdfReader(packet)
#         overlay_page = overlay_pdf.pages[0]
#
#         # Process each page
#         for page_num in range(len(existing_pdf.pages)):
#             page = existing_pdf.pages[page_num]
#
#             # Apply the overlay only to the second page (index 1)
#             if page_num == 1:
#                 page.merge_page(overlay_page)
#
#             output_pdf.add_page(page)
#
#         # Save the new PDF to the continue_word field
#         output_buffer = BytesIO()
#         output_pdf.write(output_buffer)
#         output_buffer.seek(0)
#         self.continue_word.save(f'file_{self.access_code}.pdf', File(output_buffer), save=False)
#
#         output_buffer.close()
#
#     def get_download_url(self):
#         return reverse('admin:secureword_download', args=[self.id])
#
#
#
# class SecureWord2(models.Model):
#     word_file = models.FileField(upload_to='pdf/')
#     access_code = models.CharField(max_length=4, unique=True, blank=True)
#     qr_code = models.ImageField(upload_to='qrcodes/', blank=True)
#     continue_word = models.FileField(upload_to='docs/', blank=True)
#
#     def save(self, *args, **kwargs):
#         # Save the instance first to ensure the file is saved
#         if not self.pk:  # Check if it's a new instance
#             super(SecureWord2, self).save(*args, **kwargs)
#
#         # Now that the file is saved, check if it exists
#         if not os.path.exists(self.word_file.path):
#             raise FileNotFoundError(f"The file {self.word_file.path} does not exist.")
#
#         if not self.access_code:
#             self.access_code = self.generate_unique_code()
#
#         if not self.qr_code:
#             self.generate_qr_code()
#
#         pdfmetrics.registerFont(TTFont('DejaVuSerifCondensed', 'static/ttf/DejaVuSerifCondensed.ttf'))
#         # Embed the QR code and access code into the PDF
#         self.embed_qr_code_and_access_code()
#
#         # Save the changes to the model
#         super(SecureWord2, self).save(*args, **kwargs)
#
#     def generate_unique_code(self):
#         """Generate a unique 4-digit access code."""
#         while True:
#             code = get_random_string(4, allowed_chars='0123456789')
#             if not SecureWord2.objects.filter(access_code=code).exists():
#                 return code
#
#     def generate_qr_code(self):
#         """Generate the QR code."""
#         qr = qrcode.QRCode(
#             version=2,
#             error_correction=qrcode.constants.ERROR_CORRECT_L,
#             box_size=10,
#             border=4,
#         )
#         qr_data = f"https://my.govuz.org/secure-word/login/{self.access_code}/"
#         qr.add_data(qr_data)
#         qr.make(fit=True)
#
#         img = qr.make_image(fill='black', back_color='white')
#         buffer = BytesIO()
#         img.save(buffer, format="PNG")
#         self.qr_code.save(f'{self.access_code}.png', File(buffer), save=False)
#
#     def embed_qr_code_and_access_code(self):
#         """Embed the QR code and access code only on the second page of the PDF."""
#         existing_pdf = PdfReader(self.word_file.path)
#         output_pdf = PdfWriter()
#
#         # Create a single overlay page with the QR code and access code
#         packet = BytesIO()
#         can = canvas.Canvas(packet, pagesize=letter)
#
#         # Draw the QR code and access code on the overlay page
#         can.drawImage(self.qr_code.path, x=467, y=372, width=95, height=95)  # Adjust coordinates as needed
#         can.setFont("DejaVuSerifCondensed", 22.5)
#         can.drawString(420, 410, f'{self.access_code}')  # Adjust coordinates as needed
#
#         can.save()
#
#         # Move to the beginning of the BytesIO buffer
#         packet.seek(0)
#
#         # Read the overlay page
#         overlay_pdf = PdfReader(packet)
#         overlay_page = overlay_pdf.pages[0]
#
#         # Process each page
#         for page_num in range(len(existing_pdf.pages)):
#             page = existing_pdf.pages[page_num]
#
#             # Apply the overlay only to the first page (index 0)
#             if page_num == 0:
#                 page.merge_page(overlay_page)
#
#             output_pdf.add_page(page)
#
#         # Save the new PDF to the continue_word field
#         output_buffer = BytesIO()
#         output_pdf.write(output_buffer)
#         output_buffer.seek(0)
#         self.continue_word.save(f'file__{self.access_code}.pdf', File(output_buffer), save=False)
#
#         output_buffer.close()
#
#     def get_download_url(self):
#         return reverse('admin:secureword2_download', args=[self.id])
#
#
# class SecureWord3(models.Model):
#     word_file = models.FileField(upload_to='pdf/')
#     access_code = models.CharField(max_length=4, unique=True, blank=True)
#     qr_code = models.ImageField(upload_to='qrcodes/', blank=True)
#     continue_word = models.FileField(upload_to='docs/', blank=True)
#
#     def save(self, *args, **kwargs):
#         # Save the instance first to ensure the file is saved
#         if not self.pk:  # Check if it's a new instance
#             super(SecureWord3, self).save(*args, **kwargs)
#
#         # Now that the file is saved, check if it exists
#         if not os.path.exists(self.word_file.path):
#             raise FileNotFoundError(f"The file {self.word_file.path} does not exist.")
#
#         if not self.access_code:
#             self.access_code = self.generate_unique_code()
#
#         if not self.qr_code:
#             self.generate_qr_code()
#
#         pdfmetrics.registerFont(TTFont('DejaVuSerifCondensed', 'static/ttf/DejaVuSerifCondensed.ttf'))
#         # Embed the QR code and access code into the PDF
#         self.embed_qr_code_and_access_code()
#
#         # Save the changes to the model
#         super(SecureWord3, self).save(*args, **kwargs)
#
#     def generate_unique_code(self):
#         """Generate a unique 4-digit access code."""
#         while True:
#             code = get_random_string(4, allowed_chars='0123456789')
#             if not SecureWord3.objects.filter(access_code=code).exists():
#                 return code
#
#     def generate_qr_code(self):
#         """Generate the QR code."""
#         qr = qrcode.QRCode(
#             version=2,
#             error_correction=qrcode.constants.ERROR_CORRECT_L,
#             box_size=10,
#             border=4,
#         )
#         qr_data = f"https://my.govuz.org/secure-word/login/{self.access_code}/"
#         qr.add_data(qr_data)
#         qr.make(fit=True)
#
#         img = qr.make_image(fill='black', back_color='white')
#         buffer = BytesIO()
#         img.save(buffer, format="PNG")
#         self.qr_code.save(f'{self.access_code}.png', File(buffer), save=False)
#
#     def embed_qr_code_and_access_code(self):
#         """Embed the QR code and access code only on the second page of the PDF."""
#         existing_pdf = PdfReader(self.word_file.path)
#         output_pdf = PdfWriter()
#
#         # Create a single overlay page with the QR code and access code
#         packet = BytesIO()
#         can = canvas.Canvas(packet, pagesize=letter)
#
#         # Draw the QR code and access code on the overlay page
#         can.drawImage(self.qr_code.path, x=467, y=330, width=95, height=95)  # Adjust coordinates as needed
#         can.setFont("DejaVuSerifCondensed", 22.5)
#         can.drawString(420, 372, f'{self.access_code}')  # Adjust coordinates as needed
#
#         can.save()
#
#         # Move to the beginning of the BytesIO buffer
#         packet.seek(0)
#
#         # Read the overlay page
#         overlay_pdf = PdfReader(packet)
#         overlay_page = overlay_pdf.pages[0]
#
#         # Process each page
#         for page_num in range(len(existing_pdf.pages)):
#             page = existing_pdf.pages[page_num]
#
#             # Apply the overlay only to the first page (index 0)
#             if page_num == 0:
#                 page.merge_page(overlay_page)
#
#             output_pdf.add_page(page)
#
#         # Save the new PDF to the continue_word field
#         output_buffer = BytesIO()
#         output_pdf.write(output_buffer)
#         output_buffer.seek(0)
#         self.continue_word.save(f'_file_{self.access_code}.pdf', File(output_buffer), save=False)
#
#         output_buffer.close()
#
#     def get_download_url(self):
#         return reverse('admin:secureword3_download', args=[self.id])




class Security_pdf(models.Model):
    continue_word = models.FileField(upload_to='pdf/')
    access_code = models.CharField(max_length=4, unique=True, blank=True)
    link = models.CharField(max_length=400, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Save the instance initially to get an id if it doesn't have one
        if not self.id:
            super().save(*args, **kwargs)

        # Now set the link using the assigned id
        self.link = f'https://my-govuz.org/ru/file/download/?guid={self.id}'

        # Save again to update the link
        super().save(*args, **kwargs)

