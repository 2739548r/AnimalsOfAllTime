# Generated by Django 2.2.28 on 2024-03-04 17:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='animal_images')),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('date', models.DateField(auto_now_add=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('description', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('animals', models.ManyToManyField(to='wildthoughts.Animal')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_user_lists', to='wildthoughts.UserProfile')),
                ('downvotes_by', models.ManyToManyField(related_name='downvoted_user_lists', to='wildthoughts.UserProfile')),
                ('upvoted_by', models.ManyToManyField(related_name='upvoted_user_lists', to='wildthoughts.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Discussion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('date', models.DateField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('slug', models.SlugField(unique=True)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wildthoughts.Animal')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_discussions', to='wildthoughts.UserProfile')),
                ('downvotes_by', models.ManyToManyField(related_name='downvoted_discussions', to='wildthoughts.UserProfile')),
                ('upvoted_by', models.ManyToManyField(related_name='upvoted_discussions', to='wildthoughts.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_comments', to='wildthoughts.UserProfile')),
                ('discussion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wildthoughts.Discussion')),
                ('downvotes_by', models.ManyToManyField(related_name='downvoted_comments', to='wildthoughts.UserProfile')),
                ('upvoted_by', models.ManyToManyField(related_name='upvoted_comments', to='wildthoughts.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authored_animals', to='wildthoughts.UserProfile'),
        ),
        migrations.AddField(
            model_name='animal',
            name='downvotes_by',
            field=models.ManyToManyField(related_name='downvoted_animals', to='wildthoughts.UserProfile'),
        ),
        migrations.AddField(
            model_name='animal',
            name='upvoted_by',
            field=models.ManyToManyField(related_name='upvoted_animals', to='wildthoughts.UserProfile'),
        ),
    ]
