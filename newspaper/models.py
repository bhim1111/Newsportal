from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True




class Category(TimeStampModel):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
        

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"




class Tag(TimeStampModel):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name
        


        #post - category
        #1 category can have  M post => M
        #1 post is associated to only 1 catogory => 1
        
        # User - post 
        # 1 user can ass M posts => M
        # 1 post is associated to 1 user => 1

        # post - tag
        # 1 post can have M tags => M
        #1 tag can be added to M post => M

class Post(TimeStampModel):
    STATUS_CHOICES = [
        ("active", "Active"),
        ("in_active", "inactive"),

    ]
    title =models.CharField(max_length=200)
    content = models.TextField()
    featured_image = models.ImageField(upload_to="post_images/%Y/%m/%d", blank=False)
    author = models.ForeignKey("auth.User", on_delete = models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    views_count = models.PositiveBigIntegerField(default=0)
    is_breaking_news = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank =True)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    


class Advertisement(TimeStampModel):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="advertisements/%Y/%m/%d", blank=False)


    def __str__(self):
        return self.title
    

    
    

