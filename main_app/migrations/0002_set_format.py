# Generated by Django 4.0.6 on 2022-07-14 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date Last Played')),
                ('formats', models.CharField(choices=[('MOD', 'Modern'), ('STD', 'Standard'), ('PNR', 'Pioneer'), ('LGC', 'Legacy'), ('VIN', 'Vintage'), ('PAU', 'Pauper'), ('CMD', 'Commander'), ('BRW', 'Brawl')], default='MOD', max_length=3)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.card')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
