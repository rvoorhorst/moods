from django import template

register = template.Library()


@register.simple_tag
def background_image():
    return
