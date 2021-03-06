# Generated by Django 4.0.3 on 2022-03-25 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0014_remove_post_author_delete_comment_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=150)),
                ('release_year', models.IntegerField()),
                ('director', models.CharField(max_length=100)),
                ('movie_plot', models.TextField()),
            ],
        ),
    ]
