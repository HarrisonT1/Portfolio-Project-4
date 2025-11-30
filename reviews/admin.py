from django.contrib import admin
from .models import Review, Comment

# Register your models here.


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'star_rating', 'approved', 'created_at')
    list_filter = ('approved', 'created_at', 'star_rating')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'review', 'id')
    search_fields = ('comment',)
    list_filter = ('created_at',)
