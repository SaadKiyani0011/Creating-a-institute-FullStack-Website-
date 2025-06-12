from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Enrollment(models.Model):
    ENROLLMENT_TYPES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
    ]
    
    QUALIFICATION_CHOICES = [
        ('high_school', 'High School'),
        ('diploma', 'Diploma'),
        ('bachelors', "Bachelor's Degree"),
        ('masters', "Master's Degree"),
    ]

    # Personal Information
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    # Academic Background
    last_school = models.CharField(max_length=200)
    highest_qualification = models.CharField(
        max_length=50,
        choices=QUALIFICATION_CHOICES
    )
    year_completed = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2023)
        ]
    )

    # Program Details
    program = models.CharField(max_length=100)
    enrollment_type = models.CharField(
        max_length=20,
        choices=ENROLLMENT_TYPES
    )

    # Documents
    transcript = models.FileField(upload_to='enrollments/transcripts/')
    id_proof = models.FileField(upload_to='enrollments/id_proofs/')

    # Meta
    application_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.full_name} - {self.program}"

class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name