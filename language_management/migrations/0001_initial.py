# Generated by Django 2.0.6 on 2018-07-05 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LayoutLanguages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_language', models.CharField(choices=[('en', 'English'), ('es', 'Spanish'), ('pt', 'Portuguese'), ('fr', 'French'), ('it', 'Italian'), ('ja', 'Japanese')], max_length=7)),
            ],
        ),
    ]
