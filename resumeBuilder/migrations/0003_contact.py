# Generated by Django 3.1.7 on 2021-04-10 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeBuilder', '0002_auto_20210409_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('phoneno', models.CharField(max_length=12)),
                ('msg', models.TextField()),
            ],
        ),
    ]