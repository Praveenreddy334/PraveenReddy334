# Generated by Django 4.0.1 on 2022-01-18 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapi', '0005_alter_studentdetails_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='pas1',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='gender',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
