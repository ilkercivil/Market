# Generated by Django 5.0.3 on 2024-03-25 06:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tcore', '0006_about_content_en_about_content_tr_about_title_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_en', models.CharField(max_length=200, null=True)),
                ('title_tr', models.CharField(max_length=200, null=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('content_en', ckeditor.fields.RichTextField(null=True)),
                ('content_tr', ckeditor.fields.RichTextField(null=True)),
                ('slug', models.SlugField(blank=True, editable=False, max_length=200)),
            ],
        ),
    ]
