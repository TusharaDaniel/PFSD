# Generated by Django 4.2.6 on 2024-03-09 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=255)),
                ('lyrics_by', models.CharField(max_length=255)),
                ('album', models.CharField(max_length=255)),
                ('genre_type', models.CharField(choices=[('Popmusic', 'Pop music'), ('Indianpop', 'Indian-pop'), ('Jazz', 'jazz'), ('Bollywood', 'bollywood'), ('EDM', 'edm'), ('hollywood', 'Hollywood')], max_length=20)),
            ],
        ),
    ]