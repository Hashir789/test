# Generated by Django 5.0.2 on 2024-02-26 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ABC',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ab', models.IntegerField(default=0)),
                ('bc', models.TextField(default='', max_length=1000)),
            ],
        ),
    ]
