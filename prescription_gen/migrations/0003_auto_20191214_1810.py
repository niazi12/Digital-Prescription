# Generated by Django 2.1.7 on 2019-12-14 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription_gen', '0002_prescription_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescription',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
