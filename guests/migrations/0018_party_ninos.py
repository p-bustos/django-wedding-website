# Generated by Django 3.2.9 on 2021-11-25 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0017_auto_20211124_0013'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='ninos',
            field=models.BooleanField(null=True),
        ),
    ]
