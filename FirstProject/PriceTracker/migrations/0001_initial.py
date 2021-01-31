# Generated by Django 3.1.5 on 2021-01-24 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amazon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.URLField(max_length=500)),
                ('desired_price', models.FloatField()),
                ('email', models.EmailField(max_length=254)),
                ('time', models.DateTimeField()),
            ],
        ),
    ]
