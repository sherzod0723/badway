# Generated by Django 5.0 on 2024-09-26 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_secureword3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Security_pdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_file', models.FileField(upload_to='pdf/')),
                ('access_code', models.CharField(blank=True, max_length=4, unique=True)),
            ],
        ),
    ]
