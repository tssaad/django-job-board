from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.db.models.signals import post_save
from django.dispatch import receiver



class Profile(models.Model):
    PRFUser = models.OneToOneField(User, related_name="User_profile", on_delete=models.CASCADE ,verbose_name=_("User"))
    PRFCity = models.ForeignKey('City', related_name="User_City", on_delete=models.CASCADE, verbose_name=_("City"), blank=True, null=True)
    PRFCountry = CountryField(verbose_name=_("Country"))
    PRFPhone = models.CharField(max_length=15, verbose_name=_("Phone Number"))
    PRFImage = models.ImageField(upload_to="profile/", verbose_name=_("Profile Image"))

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(PRFUser=instance)

    class Meta:
        verbose_name = _("Profile")
        verbose_name_plural = _("Profiles")

    def __str__(self):
        return str(self.PRFUser)


class City(models.Model):
    CityName = models.CharField(max_length=50, verbose_name=_("City"))

    class Meta:
        verbose_name = _("City")
        verbose_name_plural = _("Cities")

    def __str__(self):
        return self.CityName
