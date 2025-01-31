# Generated by Django 5.0.6 on 2024-09-10 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('adm_no', models.IntegerField()),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('image', models.ImageField(default='default.jpg', upload_to='profiles')),
            ],
        ),
    ]
