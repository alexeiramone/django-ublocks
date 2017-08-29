# -*- coding: utf-8 -*-
from django.db import models
from .mixins import AutomaticDatesMixin
# from django.contrib.sites.models import Site
# from django.core.validators import MaxValueValidator, MinValueValidator

# from filebrowser.fields import FileBrowseField

TEMPLATES_CHOICES = (
    ('bs3_jumbotron1','BS3 | Jumbotron 01'),
    # ('',''),
)

class Item(AutomaticDatesMixin):
    id = models.SlugField('ID', primary_key=True, max_length=128, help_text=u'Slug, should be unique')
    title = models.CharField('Title', max_length=128, blank=True, null=True)
    subtitle = models.CharField('Subtitle', max_length=256, blank=True, null=True)
    text = models.TextField('Text', blank=True, null=True)
    local_file = models.FileField('Local File or image', max_length=256, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
        ordering = ['id',]

    def __unicode__(self):
        return unicode(self.title)

# class Route(models.Model):
#     site = models.ForeignKey(Site)
#     path = models.CharField('Path', max_length=256, null=False, blank=False)

#     class Meta:
#         verbose_name = "Route"
#         verbose_name_plural = "Routes"

#     def __unicode__(self):
#         return self.site.domain + self.path

#     def get_absolute_url(self):
#         return self.path


class Block(AutomaticDatesMixin):
    # route = models.ForeignKey(Route, related_name='blocks')
    item = models.ForeignKey(Item, blank=True, null=True)
    template = models.CharField('Template', max_length=256, blank=False, null=False, choices=TEMPLATES_CHOICES)

    class Meta:
        verbose_name = "Block"
        verbose_name_plural = "Blocks"
        # ordering = ['order',]

    def __unicode__(self):
        return u'Block'
        # return u'P{!r}:ID{}'.format(self.order,self.id)

    def html_template(self):
        return u'ublocks/{}.html'.format(self.template)