from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    category_title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.category_title


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Authors(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    experience = models.TextField()
    photo = models.ImageField(upload_to='author_photos/', null=False, blank=False)


class ClassesRank(models.Model):
    class_title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.class_title


class Subjects(models.Model):
    subject_title = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.subject_title


class Video(models.Model):
    title = models.CharField(max_length=200)
    video_short_description = models.CharField(max_length=255)
    video_long_description = models.TextField()
    link = models.URLField()
    video_thumbnail = models.ImageField(upload_to='video_thumbnails/', null=False, blank=False)
    video_price = models.DecimalField(max_digits=10, decimal_places=2)
    video_discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    video_author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='videos', null=True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    class_rank = models.ForeignKey(ClassesRank, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subjects, on_delete=models.CASCADE)


class Subscribe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Foreign key to the User model
    video = models.ForeignKey(Video, on_delete=models.CASCADE)  # Foreign key to the Video model

    class Meta:
        unique_together = ('user', 'video')


class SubscriptionRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)  # Assuming Video is another model in your app
    bkash_number = models.CharField(max_length=50)
    trx_id = models.CharField(max_length=100)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField()

    def __str__(self):
        return f"Subscription Request - User: {self.user}, Video: {self.video}, Status: {self.get_status_display()}"
