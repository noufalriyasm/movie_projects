# Generated by Django 4.2.9 on 2024-02-25 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='image',
            field=models.ImageField(default='ddffdfs', upload_to='gallery'),
            preserve_default=False,
        ),
    ]
