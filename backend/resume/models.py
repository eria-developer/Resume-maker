from django.db import models
from authentication.models import  CustomUser


class Resume(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="resumes")
    title = models.CharField(max_length=254)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name="profiles")
    first_name = models.CharField(max_length=50, null=False, blank=False)
    othernames = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=False, null=False)
    website = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.othernames}"


class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name="education")
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    field_of_study = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.profile.first_name} {self.degree} from {self.institution}"


class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name="experience")
    job_title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.job_title} at {self.company}"


class Skill(models.Model):
    PROFICIENCY_LEVEL_CHOICES = (
        ("beginner", "Beginner Level"),
        ("intermediate", "Intermediate Level"),
        ("advanced", "Advanced Level"),
        ("professional", "Professional Level"),
    )

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name="skills")
    name = models.CharField(max_length=255)
    proficiency_level = models.CharField(max_length=50, blank=True, null=True, choices=PROFICIENCY_LEVEL_CHOICES)

    def __str__(self):
        return self.name


class Leadership(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name="leadership")
    role = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.role} at {self.organization}"


class Reference(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name="references")
    name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name


class Certification(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name="certifications")
    name = models.CharField(max_length=255)
    authority = models.CharField(max_length=255)
    license_number = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name="projects")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


class Language(models.Model):
    PROFICIENCY_LEVEL_CHOICES = (
        ("beginner", "Beginner Level"),
        ("intermediate", "Intermediate Level"),
        ("advanced", "Advanced Level"),
        ("fluent", "Fluent Level"),
    )

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True, related_name="languages")
    name = models.CharField(max_length=255)
    proficiency_level = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
