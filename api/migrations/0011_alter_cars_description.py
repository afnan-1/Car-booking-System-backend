# Generated by Django 3.2.5 on 2021-08-01 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_cars_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
