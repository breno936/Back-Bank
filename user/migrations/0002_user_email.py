# Generated by Django 4.1.3 on 2022-12-01 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='a@a', max_length=200),
        ),
    ]
