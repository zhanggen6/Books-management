# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-28 08:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('university', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=3, max_digits=8)),
                ('date', models.CharField(max_length=64)),
                ('author', models.ManyToManyField(to='app01.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Classify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Publish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('addr', models.CharField(max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='classify',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Classify'),
        ),
        migrations.AddField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publish'),
        ),
    ]