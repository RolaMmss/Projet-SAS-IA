# Generated by Django 4.1 on 2022-10-21 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apikeywordsmodel',
            name='api_choices',
            field=models.CharField(choices=[('s1', 's1'), ('s2', 's2'), ('s3', 's3')], max_length=50, null=True),
        ),
    ]
