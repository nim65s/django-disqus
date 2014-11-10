# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings
from django.template.loader import render_to_string

def disqus(request):
    if settings.DEBUG:
        return {'disqus': ""}
    return {'disqus': render_to_string("disqus.html", {'disqus_shortname': settings.DISQUS_SHORTNAME})}
