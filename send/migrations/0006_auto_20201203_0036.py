# Generated by Django 3.1.3 on 2020-12-02 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('send', '0005_auto_20201202_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='file',
            field=models.FileField(upload_to='file'),
        ),
        migrations.AlterField(
            model_name='data',
            name='text',
            field=models.TextField(max_length=100),
        ),
    ]