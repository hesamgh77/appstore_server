# Generated by Django 2.1.7 on 2019-04-01 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='app',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('app_description', models.CharField(blank=True, max_length=200)),
                ('creator', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=20)),
                ('download_number', models.IntegerField(default=0)),
                ('size', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='bookmark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.app')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myuser.user')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='download',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.app')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myuser.user')),
            ],
        ),
        migrations.CreateModel(
            name='set_comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.app')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myapp.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='myuser.user')),
            ],
        ),
    ]
