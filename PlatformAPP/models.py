from django.db import models

class BlogCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class BlogTag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=300, blank=True, null=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(BlogTag, through='BlogPostTag')
    image = models.ImageField(upload_to='blog_images', blank=True, null=True)

    def __str__(self):
        return self.title


class BlogPostTag(models.Model):
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    blogtag = models.ForeignKey(BlogTag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.blogpost.title} - {self.blogtag.name}"
# relation many to many 'blogpostTag'


class Programs(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    instructor = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    message = models.TextField()

    def __str__(self):
        return self.name
