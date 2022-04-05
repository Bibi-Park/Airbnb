# Generated by Django 3.1.5 on 2022-04-05 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='room',
            old_name='bath',
            new_name='baths',
        ),
        migrations.AddField(
            model_name='room',
            name='room_type',
            field=models.ManyToManyField(blank=True, to='rooms.RoomType'),
        ),
    ]
