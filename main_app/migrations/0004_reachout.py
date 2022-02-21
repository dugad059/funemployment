# Generated by Django 4.0.2 on 2022-02-21 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_jobs_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reachout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Reachout Date')),
                ('reachout_name', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.jobs')),
            ],
        ),
    ]
