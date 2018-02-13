# Generated by Django 2.0.1 on 2018-02-04 09:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iimv', '0007_auto_20180129_2254'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('date', models.DateTimeField()),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='static/events')),
            ],
        ),
        migrations.AlterField(
            model_name='updates',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2018, 2, 4, 14, 47, 4, 328838)),
        ),
    ]
