# Generated by Django 3.2 on 2021-07-01 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_projects_public'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='ibm_service_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
