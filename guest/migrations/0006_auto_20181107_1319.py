# Generated by Django 2.1.2 on 2018-11-07 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guest', '5_auto_20181107_1125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='guest',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='guest.Guest'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='guest.Room'),
        ),
    ]
