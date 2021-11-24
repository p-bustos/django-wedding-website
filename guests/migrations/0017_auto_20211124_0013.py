# Generated by Django 3.2.9 on 2021-11-24 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0016_party_rehearsal_dinner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guest',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='party',
            name='rehearsal_dinner',
        ),
        migrations.AlterField(
            model_name='guest',
            name='is_attending',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='is_child',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='is_attending',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='type',
            field=models.CharField(choices=[('Leticia', 'Leticia'), ('Esteban', 'Esteban')], max_length=10),
        ),
    ]