# Generated by Django 4.0.4 on 2022-06-06 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issues', '0003_issuecomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='issuecomment',
            name='issue',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='issues.issue'),
            preserve_default=False,
        ),
    ]
