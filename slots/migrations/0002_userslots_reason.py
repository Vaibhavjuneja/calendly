# Generated by Django 3.2.5 on 2021-07-01 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userslots',
            name='reason',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
