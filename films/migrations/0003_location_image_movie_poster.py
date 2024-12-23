# Generated by Django 5.1.2 on 2024-10-22 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_alter_ticket_destination'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='locations/'),
        ),
        migrations.AddField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='posters/'),
        ),
    ]
