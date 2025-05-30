# Generated by Django 5.2.1 on 2025-05-27 17:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('ex_date', models.DateField()),
                ('country', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('category', models.CharField(choices=[('laptop', 'laptop'), ('pc', 'pc'), ('phones', 'phones')], max_length=10)),
                ('image', models.ImageField(upload_to='products/')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapi.user')),
            ],
        ),
    ]
