# Generated by Django 2.2.4 on 2020-11-11 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=25)),
                ('lname', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=25)),
            ],
        ),
    ]
