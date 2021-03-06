# Generated by Django 4.0.1 on 2022-02-01 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_stage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stage',
            name='project',
        ),
        migrations.AddField(
            model_name='project',
            name='stages',
            field=models.ManyToManyField(to='projects.Stage'),
        ),
        migrations.AlterField(
            model_name='stage',
            name='value',
            field=models.CharField(choices=[('Ongoing', 'Ongoing'), ('complete', 'Complete')], max_length=100),
        ),
    ]
