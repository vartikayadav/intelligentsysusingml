# Generated by Django 2.0.7 on 2019-11-29 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insert_data', '0002_data_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='data',
            old_name='file',
            new_name='file1',
        ),
        migrations.AddField(
            model_name='data',
            name='file2',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
