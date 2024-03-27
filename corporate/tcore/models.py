from django.db import models
from ckeditor.fields import RichTextField  # RichTextField'ı burada içe aktarıyoruz
from django.utils.text import slugify

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()

class About(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()  # RichTextField burada doğru şekilde kullanılıyor

class Service(models.Model):
    title = models.CharField(max_length=200)
    content = RichTextField()
    slug = models.SlugField(max_length=200, blank=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)

class Slider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='slider')

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True, blank=True, editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='blogs')
    content = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    slug = models.SlugField(max_length=200, unique=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Settings(models.Model):
    logo_1=models.ImageField(upload_to='dimg',null=True ,blank=True)
    logo_2=models.ImageField(upload_to='dimg',null=True ,blank=True)
    title =models.CharField(max_length=225)
    keywords=models.CharField(max_length=225)
    description=models.CharField(max_length=225)
    phone_fixed=models.CharField(max_length=15)
    phone_mobile=models.CharField(max_length=15)
    fax=models.CharField(max_length=15)
    email=models.EmailField()
