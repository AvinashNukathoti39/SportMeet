# Generated by Django 5.1.6 on 2025-03-27 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SportMeetApp', '0029_transaction_booking_transaction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='transaction',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
    ]
