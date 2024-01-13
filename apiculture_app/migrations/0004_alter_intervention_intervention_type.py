# Generated by Django 5.0.1 on 2024-01-08 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiculture_app', '0003_remove_gathering_beehive_gathering_intervention'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervention',
            name='intervention_type',
            field=models.CharField(choices=[('RCS', 'Royal Cell Supress'), ('HC', 'Health Check'), ('SD', 'Sirop Distribution'), ('PH', 'Pose de hausses'), ('D', 'Desctruction'), ('MAE', "Multiplication artificielle de l'essaim"), ('R', 'Récolte')], max_length=3),
        ),
    ]
