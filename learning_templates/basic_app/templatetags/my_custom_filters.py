from django import template

register = template.Library()

@register.filter(name="cut")
def cut(value, arg):
    """
    this function cuts the values of itself
    :param value: string
    :param args: part of string which you want to cut it.
    :return: cutted string
    """

    return value.replace(arg, '')


# register.filter('cut', cut)
