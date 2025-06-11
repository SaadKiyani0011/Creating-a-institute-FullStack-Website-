from django.db import models
# from ckeditor.fields import RichTextField  # For rich text content

class Course(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    description = models.TextField()
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class MissionVision(models.Model):
    # mission = RichTextField()
    # vision = RichTextField()
    last_updated = models.DateTimeField(auto_now=True)

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/')
    is_ceo = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.position})"