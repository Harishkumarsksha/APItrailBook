# Generated by Django 3.0.6 on 2020-05-20 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, choices=[('EN', 'English'), ('HD', 'Hindhi')], max_length=255, null=True),
        ),
    ]
