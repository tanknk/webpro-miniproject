# Generated by Django 3.0.3 on 2020-02-21 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200222_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=models.ImageField(null=True, upload_to='picture'),
        ),
    ]
