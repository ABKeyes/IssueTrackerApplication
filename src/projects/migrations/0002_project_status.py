# Generated by Django 4.0.4 on 2022-05-30 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.CharField(default='Open', max_length=20),
        ),
    ]
