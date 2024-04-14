from django.db import models


class Category(models.Model):
    name = models.CharField(max_length = 45)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length = 200)
    headline = models.CharField(max_length = 250)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    cover_image = models.ImageField(upload_to = 'covers/')
    created_at = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    image = models.ImageField(upload_to = 'images/', blank = True, null = True)
    video_url = models.URLField(blank = True, null = True)


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']