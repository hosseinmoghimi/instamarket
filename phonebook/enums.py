from django.db.models import TextChoices
from django.utils.translation import gettext as _
class EntryDetailEnum(TextChoices):
    CELL='موبایل',_('موبایل')
    TEL='تلفن',_('تلفن')
    EMAIL='ایمیل',_('ایمیل')
    ADDRESS='آدرس',_('آدرس')
    NOTE='یادداشت',_('یادداشت')
    
