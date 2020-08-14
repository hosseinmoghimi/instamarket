from dashboard.errors import LEO_ERRORS
from django import template
register = template.Library()
from manager.enums import ContractStatusEnum


@register.filter
def to_contract_status_color(value):
    
    if value==ContractStatusEnum.INITIAL:
        return 'secondary'
    if value==ContractStatusEnum.TO_DO:
        return 'danger'
    if value==ContractStatusEnum.IN_PROGRESS:
        return 'success'
    if value==ContractStatusEnum.READY_TO_REVIEW:
        return 'primary'
    if value==ContractStatusEnum.REVIEWER_APPROVED:
        return 'success'
    if value==ContractStatusEnum.REVIEW_IN_PROGRESS:
        return 'warning'
    if value==ContractStatusEnum.DONE:
        return 'info'
    if value==ContractStatusEnum.DELIVERED:
        return 'success'
  
    return ''
