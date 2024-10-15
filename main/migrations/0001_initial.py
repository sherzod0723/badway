# Generated by Django 5.1 on 2024-08-21 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SecureWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_file', models.FileField(upload_to='pdf/')),
                ('access_code', models.CharField(blank=True, max_length=4, unique=True)),
                ('qr_code', models.ImageField(blank=True, upload_to='qrcodes/')),
                ('continue_word', models.FileField(blank=True, upload_to='docs/')),
            ],
        ),
    ]