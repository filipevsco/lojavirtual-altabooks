# Generated by Django 4.1.5 on 2023-01-29 00:58

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='imagem',
            field=stdimage.models.StdImageField(blank=True, force_min_size=False, upload_to='imagens-produtos', variations={'thumbnail': {'crop': True, 'height': 200, 'width': 300}}),
        ),
    ]