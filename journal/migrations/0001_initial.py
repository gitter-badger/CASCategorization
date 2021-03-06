# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-24 00:48
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('activity_type', models.CommaSeparatedIntegerField(max_length=3)),
                ('learning_obj', models.CommaSeparatedIntegerField(max_length=8)),
                ('start_date', models.DateField(auto_now=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('advisor_name', models.CharField(blank=True, max_length=30)),
                ('advisor_title', models.CharField(blank=True, max_length=30)),
                ('advisor_email', models.EmailField(blank=True, max_length=254)),
                ('advisor_phone', models.CharField(blank=True, max_length=12)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ('start_date',),
            },
        ),
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('advisor_type', models.IntegerField()),
                ('mk', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Coordinator',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('coordinator_type', models.IntegerField()),
                ('mk', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('entry', tinymce.models.HTMLField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('school_id', models.CharField(max_length=6)),
                ('address', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField(verbose_name='State/province')),
                ('country', models.TextField()),
            ],
            bases=('auth.group',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('personal_code', models.CharField(max_length=6)),
                ('student_id', models.CharField(max_length=4)),
                ('grad_month', models.IntegerField()),
                ('grad_year', models.IntegerField()),
                ('mk', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.School')),
                ('student_advisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='journal.Advisor')),
                ('student_coordinator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='journal.Coordinator')),
            ],
            options={
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='coordinator',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.School'),
        ),
        migrations.AddField(
            model_name='advisor',
            name='advisor_coordinator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Coordinator'),
        ),
        migrations.AddField(
            model_name='advisor',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.School'),
        ),
    ]
