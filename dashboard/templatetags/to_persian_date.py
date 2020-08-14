from django import template
register = template.Library()
from dashboard.persian import PersianCalendar

@register.filter
def to_persian_date(value):
    try:    
        a=PersianCalendar().from_gregorian(value)
        return str(a)
    except:
        return None
