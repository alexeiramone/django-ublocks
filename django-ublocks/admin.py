# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from django.core.urlresolvers import reverse

from filebrowser.fields import FileBrowseField
from amdb.core.validators import validate_filebrowser_original

from .models import Item, Block

# INLINES

# class BlockInline(admin.StackedInline):
#     model = Block
#     fields = ('order',('item','setname'),'style')
#     can_delete = True
#     extra = 0
#     sortable_field_name = 'order'


# FORMS


# MODELADMINS

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id','title','subtitle',)

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/tinymce_setup.min.js',
        ]

admin.site.register(Item,ItemAdmin)


# class RouteAdmin(admin.ModelAdmin):
#     inlines = (BlockInline,)


# admin.site.register(Route,RouteAdmin)


class BlockAdmin(admin.ModelAdmin):
    list_display = ('id','item','template','ublocks_actions')

    def ublocks_actions(self, obj):
        ublocks_actions_string = u'<a href="{}">{}</a>'.format(reverse('ublocks_test',kwargs=dict(ublock=obj.id)),'[Test IN]')
        ublocks_actions_string = u'{} <a href="{}?mode=templatetag">{}</a>'.format(ublocks_actions_string,reverse('ublocks_test',kwargs=dict(ublock=obj.id)),'[Test TT]')
        return ublocks_actions_string
    ublocks_actions.allow_tags = True
    ublocks_actions.short_description = 'Actions'

admin.site.register(Block,BlockAdmin)


# class StyleAdmin(admin.ModelAdmin):
#     list_display = ('name','template','min_items','max_items','per_row')


# admin.site.register(Style,StyleAdmin)


# class ItemSetAdmin(admin.ModelAdmin):
#     list_display = ('name',)


# admin.site.register(ItemSet,ItemSetAdmin)
