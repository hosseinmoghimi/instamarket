from django.db import models
from django.shortcuts import reverse
from django.utils.translation import gettext as _
from .enums import IconsEnum,RegionEnum,ColorEnum,ProfileStatusEnum,TransactionDirectionEnum,TransactionTypeEnum,AddressTitleEnum


class Link(models.Model):
    title=models.CharField(_("title"), max_length=50)
    url=models.CharField(_("url"), max_length=2000)
    priority=models.IntegerField(_("priority"))
    icon=models.CharField(_("icon"),choices=IconsEnum.choices,default=IconsEnum.link, max_length=50)
    color=models.CharField(_("color"),choices=ColorEnum.choices,default=ColorEnum.PRIMARY, max_length=50)
    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _("Links")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.url
