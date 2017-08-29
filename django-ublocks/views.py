# -*- coding: utf-8 -*-
from django.shortcuts import render

from .models import Block

def test(request, ublock):
    context = dict(ublock_id=ublock,mode=request.GET.get('mode','include'))
    context['ublock'] = Block.objects.get(id=ublock)
    return render(request,'ublocks_test_base.html',context)
