# Generated by Django 4.2.5 on 2023-10-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0008_anime_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='description',
            field=models.TextField(),
        ),
    ]
