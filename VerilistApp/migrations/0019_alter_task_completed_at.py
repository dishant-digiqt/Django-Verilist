# Generated by Django 3.2.7 on 2021-09-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VerilistApp', '0018_alter_task_completed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed_At',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]