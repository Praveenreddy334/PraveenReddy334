# Generated by Django 4.0.1 on 2022-01-24 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapi', '0008_assignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='assignment_num',
            field=models.BigIntegerField(),
        ),
    ]
