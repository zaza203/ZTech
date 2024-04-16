# Generated by Django 5.0.4 on 2024-04-15 14:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_remove_article_image_imagecontent_article_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagecontent',
            options={'ordering': ['article']},
        ),
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
        migrations.RemoveField(
            model_name='article',
            name='video_url',
        ),
        migrations.CreateModel(
            name='ParagraphContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
            ],
            options={
                'ordering': ['article'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='paragraph',
            field=models.ManyToManyField(related_name='paragraphs', to='articles.paragraphcontent'),
        ),
        migrations.CreateModel(
            name='SubheadingContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subheading', models.CharField(max_length=200)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
            ],
            options={
                'ordering': ['article'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='subheading',
            field=models.ManyToManyField(related_name='subheadings', to='articles.subheadingcontent'),
        ),
        migrations.CreateModel(
            name='VideoContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.URLField()),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.article')),
            ],
            options={
                'ordering': ['article'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='video_url',
            field=models.ManyToManyField(blank=True, null=True, related_name='videos', to='articles.videocontent'),
        ),
    ]
