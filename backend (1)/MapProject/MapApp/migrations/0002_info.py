# Generated by Django 4.0.4 on 2022-05-28 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MapApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entrance', models.TextField()),
                ('lounge', models.TextField()),
                ('photo', models.ImageField(upload_to='')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MapApp.school')),
            ],
        ),
    ]
