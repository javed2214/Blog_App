# Generated by Django 2.1.4 on 2019-07-27 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogapp',
            name='image',
            field=models.ImageField(default='/images/x.jpg', upload_to='images/'),
        ),
    ]
