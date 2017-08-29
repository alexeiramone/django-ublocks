# -*- coding: utf-8 -*-
from django import template
# from django.conf import settings

from ..models import Block

register = template.Library()

@register.inclusion_tag('ublocks_tag_wrapper.html')
def ublock(id):
    context = {}
    context['ublock'] = Block.objects.get(id=id)
    return context
