# Generated by Django 3.0.7 on 2020-06-22 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntentDB',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('intent', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='QueryDB',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('query', models.TextField()),
                ('intent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatapp.IntentDB')),
            ],
        ),
    ]
