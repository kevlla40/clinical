# Generated by Django 3.2.25 on 2024-06-25 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_alter_patientdischargedetails_assignednursename'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='assignedNurse',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patients', to='hospital.nurse'),
        ),
    ]