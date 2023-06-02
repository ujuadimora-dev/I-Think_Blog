from django.contrib import admin

# Register your models here.
from .models import Post
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')


# admin.site.register(Post).