from django.db.models import TextChoices
from django.utils.translation import gettext as _
class ContractStatusEnum(TextChoices):
    INITIAL='جدید',_('جدید')
    TO_DO='آماده واگذاری',_('آماده واگذاری')
    IN_PROGRESS='در حال انجام',_('در حال انجام')
    READY_TO_REVIEW='آماده بررسی',_('آماده بررسی')
    REVIEW_IN_PROGRESS='در حال بررسی',_('در حال بررسی')
    REVIEWER_APPROVED='تایید شده',_('تایید شده')
    DONE='انجام شده',_('انجام شده')
    DELIVERED='تحویل شده',_('تحویل شده')