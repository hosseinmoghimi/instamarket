from dashboard.errors import LEO_ERRORS
from django import template
register = template.Library()
from dashboard.constants import CURRENCY



@register.filter
def to_price(value):
    """converts int to string"""  
    try:
        sign=''
        if value<0:
            value=0-value
            sign='- '
        a=separate(value)
        return sign+a+' '+CURRENCY
    except:
        return LEO_ERRORS.error_to_price_template_tag


def separate(price):
    
    try:
        price=int(price)
    except:
        return None
    
    if price<1000:
        return str(price)
    else:
        return separate(price/1000)+','+str(price)[-3:]
