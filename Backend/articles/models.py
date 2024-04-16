from django.db import models


class Category(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 200)
    headline = models.CharField(max_length = 250, null = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    cover_image = models.ImageField(upload_to = 'covers/')
    created_at = models.DateTimeField(auto_now_add = True)
    subheading = models.ManyToManyField('SubheadingContent', related_name = 'subheadings')
    paragraph = models.ManyToManyField('ParagraphContent', related_name = 'paragraphs')
    image = models.ManyToManyField('ImageContent', related_name='images')
    video_url = models.ManyToManyField('VideoContent', related_name='videos', blank = True, null = True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']

class ImageContent(models.Model):
    image = models.ImageField(upload_to = 'images/', blank = True, null = True)
    article = models.ForeignKey(Article, on_delete = models.CASCADE)

    class Meta:
        ordering = ['article']

class VideoContent(models.Model):
    video_url = models.URLField()
    article = models.ForeignKey(Article, on_delete = models.CASCADE)

    def __str__(self):
        return self.video_url

    class Meta:
        ordering = ['article']

class SubheadingContent(models.Model):
    subheading = models.CharField(max_length = 200)
    article = models.ForeignKey(Article, on_delete = models.CASCADE)

    def __str__(self):
        return self.subheading

    class Meta:
        ordering = ['article']

class ParagraphContent(models.Model):
    paragraph = models.TextField()
    article = models.ForeignKey(Article, on_delete = models.CASCADE)


    def __str__(self):
        return self.paragraph

    class Meta:
        ordering = ['article']