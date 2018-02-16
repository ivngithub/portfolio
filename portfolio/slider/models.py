from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey


class SliderPage(Page):

    content_panels = Page.content_panels + [

        InlinePanel('slider_items', label="Слайдер"),  # добавляем блок управления слайдером
    ]


class LinkFields(models.Model):

    slide_title = models.CharField(
        verbose_name=_('Title to slide'),
        max_length=128,
        help_text=_("Title to slide may be maximum 128 characters")
    )
    slide_description = models.CharField(
        verbose_name=_('Description to slide'),
        max_length=128,
        help_text=_("Description to slide may be maximum 128 characters")
    )
    link_external = models.URLField("URL", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        else:
            return self.link_external

    panels = [
        FieldPanel('slide_title'),
        FieldPanel('slide_description'),
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
    ]

    class Meta:
        abstract = True


class SliderItem(LinkFields):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    LinkFields.panels += [
        ImageChooserPanel('image')
    ]

    class Meta:
        abstract = True


class SliderPageItem(Orderable, SliderItem):
    page = ParentalKey('SliderPage', related_name='slider_items')
