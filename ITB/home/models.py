from django.db import models

# Create your models here.
from django.db import models # Django ka models import karna parhta ha taake ham database ke liye models bana sakein
from ckeditor.fields import RichTextField  # Rich text fields sa ham bold ittalic wagara wla text b likh sakta ha or isko use karna ka leya cheditor wali pip install karni parhte ha 

class Course(models.Model): # Course model banaya jata ha taake ham courses ki details store kar sakein 
    title = models.CharField(max_length=200) # Course ka title store karne ke liye
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class") # Font Awesome icon class store karne ke liye 
    image = models.ImageField(upload_to='media/')  # Course ki image store karne ke liye  
    description = models.TextField()
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class MissionVision(models.Model):
    mission = RichTextField()
    vision = RichTextField()
    last_updated = models.DateTimeField(auto_now=True)

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    is_ceo = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} ({self.position})"