# Generated by Django 4.0.6 on 2022-08-05 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bienvenue',
            name='image',
        ),
        migrations.AddField(
            model_name='bienvenue',
            name='mail',
            field=models.EmailField(default='test@teto.com', max_length=254, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bienvenue',
            name='mailo',
            field=models.EmailField(default='test@testo.com', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
