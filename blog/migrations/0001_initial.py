# Generated by Django 2.2.1 on 2019-09-29 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_blog', models.ImageField(upload_to='images/')),
                ('title', models.CharField(max_length=50)),
                ('pub_date', models.DateField(auto_now=True)),
                ('body', models.CharField(max_length=200)),
            ],
        ),
    ]