# Generated by Django 4.0.1 on 2022-01-19 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapi', '0006_studentdetails_pas1_alter_studentdetails_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='first_name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='last_name',
            field=models.CharField(max_length=40),
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=40)),
                ('task_start_date', models.DateField()),
                ('complete_by', models.DateField()),
                ('task_priority', models.CharField(max_length=10)),
                ('many_students', models.ManyToManyField(to='studentapi.StudentDetails')),
            ],
        ),
    ]
