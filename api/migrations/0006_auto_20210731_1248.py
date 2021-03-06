# Generated by Django 3.2.5 on 2021-07-31 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_cars_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='numReviews',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='cars',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]
