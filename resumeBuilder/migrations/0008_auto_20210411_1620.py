# Generated by Django 3.1.7 on 2021-04-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeBuilder', '0007_auto_20210411_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='highSchoolPassingYear',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='highSchoolStartingYear',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='intermediatePassingYear',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='intermediateStartingYear',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='jobEndDate',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='jobStartDate',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='projectEndDate',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='projectStartDate',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='univPassingYear',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='univStartingYear',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]