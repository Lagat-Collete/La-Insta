# Generated by Django 3.2.9 on 2022-06-08 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='likes',
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.CharField(max_length=200),
        ),
    ]