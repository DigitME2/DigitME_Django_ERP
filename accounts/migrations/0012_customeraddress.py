# Generated by Django 3.1.5 on 2021-03-19 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210319_1011'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addressline1', models.CharField(max_length=200, null=True)),
                ('county', models.CharField(max_length=30, null=True)),
                ('postcode', models.CharField(max_length=10, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
