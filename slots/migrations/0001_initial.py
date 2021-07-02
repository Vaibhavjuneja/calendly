# Generated by Django 3.2.5 on 2021-07-01 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSlots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('slot_booked_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.userprofile')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_profile', to='accounts.userprofile')),
            ],
        ),
    ]
