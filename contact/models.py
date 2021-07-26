from django.db import models
from django.db.models.fields import CharField, EmailField
from django.utils.translation import gettext_lazy as _

class Info(models.Model):
    INFAddress = models.CharField(max_length=50, verbose_name=_("Address"))
    INFPhone = models.CharField(max_length=50, verbose_name= _("Phone Number"))
    INFEmail = models.EmailField(verbose_name=_("Email"), max_length=254)
    

    class Meta:
        verbose_name = _("Information")
        verbose_name_plural = _("Information")

    def __str__(self):
        return self.INFEmail



