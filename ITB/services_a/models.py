from django.db import models
from ckeditor.fields import RichTextField

class Service(models.Model):
    SERVICE_TYPES = [
        ('corporate', 'Corporate Training'),
        ('bootcamp', 'Career Bootcamp'),
        ('certification', 'Certification Prep'),
        ('internship', 'Internship Program'),
        ('faculty', 'Faculty Development'),
        ('lab', 'Lab Infrastructure'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPES)
    icon_class = models.CharField(max_length=50, default='fas fa-circle')
    short_description = models.TextField()
    full_description = RichTextField()
    is_featured = models.BooleanField(default=False)
    badge_text = models.CharField(max_length=50, blank=True)
    display_order = models.PositiveIntegerField(default=0)
    cta_text = models.CharField(max_length=50, default='Learn More')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['display_order', 'title']

    def __str__(self):
        return self.title

class ServiceFeature(models.Model):
    service = models.ForeignKey(Service, related_name='features', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.service.title} - Feature {self.order}"