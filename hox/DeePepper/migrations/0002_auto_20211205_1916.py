# Generated by Django 3.2.9 on 2021-12-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeePepper', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='content',
        ),
        migrations.AlterField(
            model_name='fileupload',
            name='title',
            field=models.TextField(max_length=10, null=True),
        ),
    ]