# Generated by Django 4.1.7 on 2023-04-02 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_scholarship_aadhar_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholarship',
            name='aadhar',
        ),
        migrations.RemoveField(
            model_name='scholarship',
            name='birth_certificate',
        ),
        migrations.RemoveField(
            model_name='scholarship',
            name='pan',
        ),
        migrations.RemoveField(
            model_name='scholarship',
            name='passport',
        ),
        migrations.RemoveField(
            model_name='scholarship',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='scholarship',
            name='sign',
        ),
    ]
