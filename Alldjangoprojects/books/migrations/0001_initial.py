# Generated by Django 3.1.2 on 2020-10-27 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=70)),
                ('subtitle', models.CharField(default='', max_length=200)),
                ('author', models.CharField(default='', max_length=50)),
                ('isbn', models.CharField(default='', max_length=80)),
            ],
        ),
    ]
