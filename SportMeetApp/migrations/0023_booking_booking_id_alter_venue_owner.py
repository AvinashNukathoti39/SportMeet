# Generated by Django 5.1.6 on 2025-03-21 10:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SportMeetApp', '0022_rename_mode_of_pyment_booking_mode_of_payment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='booking_id',
            field=models.CharField(blank=True, editable=False, max_length=10, null=True, unique=True, verbose_name='Booking Id'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='venues', to='SportMeetApp.venueownerprofile', verbose_name='ID'),
        ),
    ]
