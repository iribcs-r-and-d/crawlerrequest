# Generated by Django 3.0 on 2020-07-05 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=200, null=True, unique=True, verbose_name='KeyWord')),
                ('res_id', models.IntegerField(null=True, unique=True, verbose_name='Res_Id')),
            ],
        ),
    ]
