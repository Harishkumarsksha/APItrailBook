# Generated by Django 3.0.6 on 2020-05-20 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(blank=True, max_length=255, null=True)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('prcie', models.FloatField(blank=True, null=True)),
                ('language', models.CharField(blank=True, max_length=255, null=True)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
                ('date_reviewed', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
