from django import forms
from django.db import models
from django.utils.text import capfirst
from django.utils.translation import ugettext_lazy as _
from django.template.loader import render_to_string

from feincms.module.blog.models import Entry, EntryAdmin
from feincms.module.page.models import Page
from feincms.content.raw.models import RawContent
from feincms.content.image.models import ImageContent
from feincms.content.medialibrary.models import MediaFileContent
from feincms.content.application.models import ApplicationContent
from feincms.module.page.extensions.navigation import NavigationExtension, PagePretender
from feincms.content.application.models import reverse
import feincms.templatetags.feincms_thumbnail

import mptt


Page.register_templates({
    'key': 'base',
    'title': 'Base Template',
    'path': 'base.html',
    'regions': (
        ('main', 'Main region'),
        ('sidebar', 'Sidebar', 'inherited'),
        ),
    })

from feincms.module.medialibrary.models import Category

class Image:
    def __init__(self, url, thumb, caption, description):
        self.url = url
        self.thumb = thumb
        self.caption = caption
        self.description = description


class SlideshowContent(models.Model):
    category = models.ForeignKey(Category)
    show_thumbnails = models.BooleanField()
    autoplay = models.BooleanField()
    enable_lightbox = models.BooleanField()
    delay = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()

    class Meta:
        abstract = True

    def render(self, **kwargs):

        images = []
        
        for img in self.category.mediafile_set.all():
            thumb = feincms.templatetags.feincms_thumbnail.thumbnail(img.file.name, '240x120')
            caption = img.translation.caption
            description = img.translation.description

            img = Image(img.file.url, thumb, caption, description)
            
            print dir(img)
            
            images.append(img)

        return render_to_string('slideshow/slideshow.html', {
            'images': images,
            'delay': self.delay,
            'width': self.width,
            'height': self.height,
            'show_thumbnails': self.show_thumbnails,
            'autoplay': self.autoplay,
            'enable_lightbox': self.enable_lightbox
        })


Page.create_content_type(SlideshowContent)


Page.create_content_type(RawContent)
MediaFileContent.default_create_content_type(Page)
Page.create_content_type(ImageContent, POSITION_CHOICES=(
    ('default', 'Default position'),
    ))

def get_admin_fields(form, *args, **kwargs):
    return {
        'exclusive_subpages': forms.BooleanField(
            label=capfirst(_('exclusive subpages')),
            required=False,
            initial=form.instance.parameters.get('exclusive_subpages', False),
            help_text=_('Exclude everything other than the application\'s content when rendering subpages.'),
            ),
    }

Page.create_content_type(ApplicationContent, APPLICATIONS=(
    ('blog_urls', 'Blog', {'admin_fields': get_admin_fields}),
    ('doc_urls', 'Sphinx Documentation', {'admin_fields': get_admin_fields}),
    ))


Entry.register_regions(
    ('main', 'Main region'),
    )
Entry.create_content_type(RawContent)
Entry.create_content_type(ImageContent, POSITION_CHOICES=(
    ('default', 'Default position'),
    ))


class BlogEntriesNavigationExtension(NavigationExtension):
    """
    Extended navigation for blog entries.

    It would be added to 'Blog' page properties in admin.
    """
    name = _('all blog entries')

    def children(self, page, **kwargs):
        for entry in Entry.objects.all():
            yield PagePretender(
                title=entry.title,
                url=reverse('blog_urls/blog_entry_details', kwargs={'object_id': entry.id}),
                )

Page.register_extensions('navigation')


try:
    from mptt.models import MPTTModel as base
    mptt_register = False
except ImportError:
    base = models.Model
    mptt_register = True

class Category(base):
    name = models.CharField(max_length=20)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children')

    class Meta:
        ordering = ['tree_id', 'lft']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name

if mptt_register:
    mptt.register(Category)

# add m2m field to entry so it shows up in entry admin
Entry.add_to_class('categories', models.ManyToManyField(Category, blank=True, null=True))
EntryAdmin.list_filter += ('categories',)
