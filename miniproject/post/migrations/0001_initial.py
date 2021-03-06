# Generated by Django 3.0.3 on 2020-02-21 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('text_book', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('S', 'sell'), ('B', 'buy')], max_length=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('picture', models.ImageField(upload_to='book_picture')),
                ('status', models.CharField(choices=[('OPEN', 'open'), ('CLOSE', 'close')], max_length=5)),
                ('create_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='authen.User')),
            ],
        ),
    ]
