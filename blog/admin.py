from django.contrib import admin
from .models import Post, Categoria, Tag

admin.site.register(Post)
admin.site.register(Categoria)
admin.site.register(Tag)