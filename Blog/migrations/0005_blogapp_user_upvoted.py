# Generated by Django 2.1.4 on 2019-07-27 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_blogapp_upvote'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogapp',
            name='user_upvoted',
            field=models.TextField(default=''),
        ),
    ]