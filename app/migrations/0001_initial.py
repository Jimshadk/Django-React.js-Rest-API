# Generated by Django 5.0.7 on 2024-07-11 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='images/')),
            ],
            options={
                'db_table': 'Book',
            },
        ),
    ]