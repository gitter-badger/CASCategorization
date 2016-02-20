# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-19 23:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('activity_type', models.CharField(max_length=3)),
                ('learning_obj', models.CharField(max_length=8)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'ordering': ('start_date',),
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Cat',
        ),
        migrations.AddField(
            model_name='activity',
            name='entries',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Entry'),
        ),
    ]