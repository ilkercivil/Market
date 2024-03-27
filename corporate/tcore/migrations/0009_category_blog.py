# Generated by Django 5.0.3 on 2024-03-27 06:10

import ckeditor.fields
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcore', '0008_slider'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('name_en', models.CharField(max_length=100, null=True)),
                ('name_tr', models.CharField(max_length=100, null=True)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_tr', models.CharField(max_length=200, null=True)),
                ('image', models.ImageField(upload_to='blogs')),
                ('content', ckeditor.fields.RichTextField()),
                ('content_en', ckeditor.fields.RichTextField(null=True)),
                ('content_tr', ckeditor.fields.RichTextField(null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('tags', models.CharField(max_length=100)),
                ('views', models.IntegerField(default=0)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=200, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcore.category')),
            ],
        ),
    ]
