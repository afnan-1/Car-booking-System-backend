# Generated by Django 3.2.5 on 2021-07-30 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210730_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='mobile_no',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
