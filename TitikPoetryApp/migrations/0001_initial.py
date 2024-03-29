# Generated by Django 3.1.6 on 2021-05-19 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('contact', models.EmailField(max_length=50)),
                ('sex', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('RecId', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='TitikPoetryApp.recruit')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_tula', models.CharField(max_length=50)),
                ('text', models.TextField(default='')),
                ('video_file', models.FileField(blank=True, null=True, upload_to='post_files')),
                ('book_donation', models.ImageField(upload_to=None)),
                ('integer', models.IntegerField(null=True)),
                ('comment', models.CharField(max_length=50)),
                ('user', models.ManyToManyField(to='TitikPoetryApp.Recruit')),
            ],
        ),
        migrations.CreateModel(
            name='Admindoing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('integer', models.IntegerField(null=True)),
                ('comment', models.CharField(max_length=50)),
                ('publications', models.ManyToManyField(to='TitikPoetryApp.Dmin')),
            ],
        ),
    ]
