from django.db import models
from .enums import ContractStatusEnum
from dashboard.enums import ColorEnum,IconsEnum
from django.shortcuts import reverse
from django.utils.translation import gettext as _
class Contract(models.Model):
    title=models.CharField(_("title"), max_length=50)
    project=models.ForeignKey("Project", verbose_name=_("project"), on_delete=models.CASCADE)
    contractor=models.ForeignKey("dashboard.Profile", verbose_name=_("contractor"),null=True,blank=True, on_delete=models.CASCADE)   
    status=models.CharField(_("status"), choices=ContractStatusEnum.choices,default=ContractStatusEnum.INITIAL,max_length=50)
    amount=models.IntegerField(_("amount"),default=0)
    color=models.CharField(_("color"),choices=ColorEnum.choices,default=ColorEnum.PRIMARY, max_length=50)
    icon=models.CharField(_("icon"),choices=IconsEnum.choices,default=IconsEnum.link, max_length=50)
    class Meta:
        verbose_name = _("Contract")
        verbose_name_plural = _("Contracts")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("manager:contract", kwargs={"contract_id": self.pk})


class Project(models.Model):
    color=models.CharField(_("color"),choices=ColorEnum.choices,default=ColorEnum.PRIMARY, max_length=50)
    icon=models.CharField(_("icon"),choices=IconsEnum.choices,default=IconsEnum.link, max_length=50)
    employer=models.ForeignKey("dashboard.Profile", verbose_name=_("employer"),blank=True,null=True, on_delete=models.CASCADE)
    title=models.CharField(_("title"), max_length=200)
    documents=models.ManyToManyField("dashboard.Document",blank=True, verbose_name=_("documents"))

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("manager:project", kwargs={"project_id": self.pk})

