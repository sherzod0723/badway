# Generated by Django 5.0 on 2024-09-26 13:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_security_pdf'),
    ]

    operations = [
        migrations.RenameField(
            model_name='security_pdf',
            old_name='pdf_file',
            new_name='continue_word',
        ),
    ]
