# Generated by Django 4.0 on 2021-12-11 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=100)),
                ('name', models.CharField(default='', max_length=100)),
                ('img', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('manufacture', models.CharField(default='', max_length=100)),
                ('price', models.IntegerField(default=0)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
    ]