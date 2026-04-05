from django.contrib import admin

# Register your models here.
# blog/admin.py
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at')