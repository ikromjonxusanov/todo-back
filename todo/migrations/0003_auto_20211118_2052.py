# Generated by Django 3.2.9 on 2021-11-18 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_auto_20211114_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('day', models.CharField(max_length=100)),
                ('reminder', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='TodoList',
        ),
    ]
