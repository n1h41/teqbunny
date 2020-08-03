# Generated by Django 3.0.5 on 2020-07-30 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project_upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=250)),
                ('project_description', models.TextField(max_length=2000)),
                ('project_role', models.CharField(max_length=250)),
                ('project_client_name', models.CharField(max_length=250)),
                ('project_client_link', models.URLField()),
                ('project_file', models.FileField(upload_to='project_files')),
                ('project_cover_image', models.ImageField(upload_to='cover_images')),
            ],
        ),
    ]
