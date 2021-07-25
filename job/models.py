from django.db import models
from django.db.models import base
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.contrib.auth.models import User
from django_countries.fields import CountryField

# Create your models here.
def image_upload(instance, filename):
    imagename, extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

JOB_TYPES = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

class Job(models.Model):
    JOBowner = models.ForeignKey(User, related_name="job_owner", on_delete=models.CASCADE, verbose_name=_("Job Owner"))
    JOBTitle = models.CharField(max_length=100, verbose_name=_("Title"))
    PRFCountry = CountryField(blank=True, null=True, verbose_name=_("Country"))
    JOBJobtype = models.CharField(max_length=15, choices=JOB_TYPES,verbose_name=_('Job Type'))
    JOBDescription = models.TextField(max_length=1000, verbose_name=_("Description"))
    JOBCreated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date Created"))
    JOBVacancy = models.IntegerField(default=1, verbose_name=_("Vacancy"))
    JOBSalary = models.IntegerField(default=0, verbose_name=_("Salary"))
    JOBExperience = models.IntegerField(default=1, verbose_name=_("Experience"))
    JOBCategory = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_("Category"))
    JOBImage = models.ImageField(upload_to=image_upload, blank=True, null=True, verbose_name=_("Image"))

    JOBSlug = models.SlugField(blank=True, null=True, verbose_name=_("Slug"))

    def save(self, *args, **kwargs):
        self.JOBSlug=slugify(self.JOBTitle)
        super(Job, self).save(*args, **kwargs)

    class Meta:
        verbose_name= _("Job")
        verbose_name_plural = _("Jobs")

    def __str__(self):
        return self.JOBTitle


class Category(models.Model):
    CATName = models.CharField(max_length=50, verbose_name=_("Category Name")) 

    class Meta:
        verbose_name= _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.CATName

class Applicatiion(models.Model):
    APPJob = models.ForeignKey('Job', related_name="Job_application", on_delete=models.CASCADE, verbose_name=_("Job"))
    APPName=models.CharField(max_length=50, verbose_name=_("Name"))
    APPEmail=models.EmailField(max_length=50, verbose_name=_("Email"))
    APPurl=models.URLField(verbose_name=_("URL"))
    APPCV=models.FileField(upload_to="apply/", verbose_name=_("CV"))
    APPCOver_letter=models.TextField(max_length=1000, verbose_name=_("Cover Letter"))
    APPCreated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date Created"))

    class Meta:
        verbose_name = _("Applicatiion")
        verbose_name_plural = _("Applicatiions")

    def __str__(self):
        return self.APPName
