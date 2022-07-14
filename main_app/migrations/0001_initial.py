# Generated by Django 4.0.6 on 2022-07-14 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('power', models.IntegerField()),
                ('toughness', models.IntegerField()),
            ],
        ),
    ]
