from django.contrib import admin
from .models import Post,Comment,Portfolio,About

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','slug','author','publish','status']
    list_filter = ['status','created','publish','author']
    search_fields = ['title','body']
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status','publish']
    show_facets = admin.ShowFacets.ALWAYS

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','post','created','active','updated']
    list_filter = ['active','created','updated']
    search_fields = ['name','email','body']
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name','image']

@admin.register(About)
class AboutMe(admin.ModelAdmin):
    list_display = ['name','created_at','date_of_birth']



