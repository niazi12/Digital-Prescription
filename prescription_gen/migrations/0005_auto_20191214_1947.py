# Generated by Django 2.1.7 on 2019-12-14 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('prescription_gen', '0004_auto_20191214_1938'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prescription',
            name='medicines',
        ),
        migrations.AddField(
            model_name='prescriptionmedicine',
            name='prescription',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='pr_med', to='prescription_gen.Prescription'),
            preserve_default=False,
        ),
    ]