# Generated by Django 2.0.2 on 2018-09-14 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Body', models.CharField(max_length=100)),
                ('Blog_Image', models.ImageField(upload_to='')),
            ],
        ),
    ]
