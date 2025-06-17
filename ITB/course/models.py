from django.db import models
from django.urls import reverse

class CourseCategory(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    LEVEL_CHOICES = [
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]

    BADGE_CHOICES = [
        ('bestseller', 'Bestseller'),
        ('new', 'New'),
        ('popular', 'Popular'),
        ('job_ready', 'Job Ready'),
        ('limited', 'Limited Seats'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    short_description = models.TextField()
    full_description = models.TextField()
    duration_weeks = models.PositiveIntegerField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    image = models.ImageField(upload_to='courses/', default='courses/default.jpg')  # updated upload path
    original_price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    current_price = models.DecimalField(max_digits=6, decimal_places=2)
    is_certified = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    badge = models.CharField(max_length=20, blank=True, choices=BADGE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_featured', 'title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})

    def get_badge_display(self):
        return dict(self.BADGE_CHOICES).get(self.badge, '')  # fallback if badge is empty

    def get_level_display(self):
        return dict(self.LEVEL_CHOICES).get(self.level, 'Unknown')
