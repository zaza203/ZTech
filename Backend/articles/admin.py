from django.contrib import admin

from .models import *

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(ImageContent)
admin.site.register(VideoContent)
admin.site.register(SubheadingContent)
admin.site.register(ParagraphContent)

