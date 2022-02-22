# Generated by Django 4.0.2 on 2022-02-21 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_reachout'),
    ]

    operations = [
        migrations.AddField(
            model_name='reachout',
            name='notes',
            field=models.TextField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Response Date')),
                ('responce_name', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('notes', models.TextField(max_length=250)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.jobs')),
            ],
        ),
    ]