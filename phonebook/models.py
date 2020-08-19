from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext as _
from .enums import EntryDetailEnum

class EntryDetail(models.Model):
    entry_name=models.CharField(_("entry_name"),choices=EntryDetailEnum.choices,default=EntryDetailEnum.CELL, max_length=50)
    entry_value=models.CharField(_("entry_value"), max_length=50)

    class Meta:
        verbose_name = _("EntryDetail")
        verbose_name_plural = _("EntryDetails")

    def __str__(self):
        return f'{self.entry_name} : {self.entry_value}'

    def get_absolute_url(self):
        return reverse("EntryDetail_detail", kwargs={"pk": self.pk})



class Entry(models.Model):
    profile=models.ForeignKey("dashboard.Profile", verbose_name=_("Profile"), on_delete=models.CASCADE)
    first_name=models.CharField(_("first_name"), max_length=50,null=True,blank=True)
    last_name=models.CharField(_("first_name"), max_length=50,null=True,blank=True)
    company=models.CharField(_("company"),null=True,blank=True, max_length=50)
    details=models.ManyToManyField("EntryDetail",blank=True, verbose_name=_("details"))
    class Meta:
        verbose_name = _("Entry")
        verbose_name_plural = _("Entrys")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("phonebook:entry", kwargs={"entry_id": self.pk})
