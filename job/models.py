from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

JOB_TYPES = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
class Job(models.Model):
    JOBTitle = models.CharField(max_length=100, verbose_name=_("Title"))
    # location = 
    JOBJobtype = models.CharField(max_length=15, choices=JOB_TYPES,verbose_name=_('Job Type'))
    JOBDescription = models.TextField(max_length=1000, verbose_name=_("Description"))
    JOBCreated_at = models.DateTimeField(auto_now=True, verbose_name=_("Date Created"))
    JOBVacancy = models.IntegerField(default=1, verbose_name=_("Vacancy"))
    JOBSalary = models.IntegerField(default=0, verbose_name=_("Salary"))
    JOBExperience = models.IntegerField(default=1, verbose_name=_("Experience"))
    JOBCategory = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name=_("Category"))

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

