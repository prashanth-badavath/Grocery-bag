# Generated by Django 3.2.6 on 2021-08-14 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=100)),
                ('item_quantity', models.IntegerField(max_length=100)),
                ('item_status', models.CharField(max_length=100)),
                ('date', models.DateTimeField(max_length=100)),
            ],
        ),
    ]
