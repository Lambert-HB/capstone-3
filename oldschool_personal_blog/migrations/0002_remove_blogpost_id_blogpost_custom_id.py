# Generated by Django 5.1.3 on 2025-02-11 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oldschool_personal_blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='id',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='custom_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
