# Generated by Django 4.0.4 on 2022-06-02 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salons', '0007_remove_salon_service'),
        ('service', '0007_remove_service_salon'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='salon',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='salons.salon'),
            preserve_default=False,
        ),
    ]
