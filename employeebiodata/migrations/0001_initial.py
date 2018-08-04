# Generated by Django 2.1 on 2018-08-04 02:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employeebiodata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=220)),
                ('lastname', models.CharField(max_length=220)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('email', models.CharField(max_length=60, unique=True)),
                ('dateCreated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('dateUpdated', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
