# Generated by Django 2.0.2 on 2018-03-10 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple3', '0002_auto_20180310_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jsonmodel',
            old_name='Gas_C2H5OH',
            new_name='gas_c2h5oh',
        ),
        migrations.RenameField(
            model_name='jsonmodel',
            old_name='Gas_C3H8',
            new_name='gas_c3h8',
        ),
        migrations.RenameField(
            model_name='jsonmodel',
            old_name='Gas_C4H10',
            new_name='gas_c4h10',
        ),
        migrations.RenameField(
            model_name='jsonmodel',
            old_name='Gas_CH4',
            new_name='gas_ch4',
        ),
        migrations.RenameField(
            model_name='jsonmodel',
            old_name='Gas_CO',
            new_name='gas_co',
        ),
        migrations.RenameField(
            model_name='jsonmodel',
            old_name='Temperature_i2c',
            new_name='temperature_i2c',
        ),
    ]
