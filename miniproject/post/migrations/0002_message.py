# Generated by Django 3.0.3 on 2020-02-21 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0001_initial'),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authen.User')),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='post.Post')),
            ],
        ),
    ]
