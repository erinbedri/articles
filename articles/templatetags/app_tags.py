from hashlib import md5
from django import template

register = template.Library()


@register.filter
def gravatar(user, size=35):
    email = str(user.email.strip().lower()).encode('utf-8')
    email_hash = md5(email).hexdigest()
    url = f'//www.gravatar.com/avatar/{email_hash}?s={size}&d=identicon&r=PG'
    return url

