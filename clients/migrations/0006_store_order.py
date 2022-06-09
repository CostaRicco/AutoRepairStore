# Generated by Django 4.0.4 on 2022-06-02 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_remove_service_salon'),
        ('salons', '0005_alter_salon_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='salon',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='service.service', verbose_name='Услуга'),
            preserve_default=False,
        ),
    ]