# Generated by Django 3.2.25 on 2024-06-25 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0021_patient_assignednurse'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='nurse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='hospital.nurse'),
        ),
    ]
