from django.contrib import admin
from .models import BlogCategory, BlogTag, BlogPost, BlogPostTag, Programs, ContactUs

admin.site.register(BlogCategory)
admin.site.register(BlogTag)
admin.site.register(BlogPost)
admin.site.register(BlogPostTag)
admin.site.register(Programs)
admin.site.register(ContactUs)
