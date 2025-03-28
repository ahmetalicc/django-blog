# Generated by Django 5.1.7 on 2025-03-17 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_commentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'contact',
            },
        ),
    ]
