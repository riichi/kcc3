import datetime

from django import template

register = template.Library()


PLACEHOLDER = "\u2014"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"


@register.simple_tag(name="placeholder")
def placeholder_tag() -> str:
    return PLACEHOLDER


@register.filter(name="placeholder")
def placeholder_filter(data: str | None) -> str:
    return data if data else PLACEHOLDER


@register.filter
def dateformat(date: datetime.date | None) -> str:
    if date is None:
        return PLACEHOLDER
    return date.strftime(DEFAULT_DATE_FORMAT)
