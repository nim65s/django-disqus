django-disqus
=============

My tiny disqus scripts

HOWTO
=============

In settings.py, add
- "django-disqus" in INSTALLED_APPS
- "django-disqus.contixt-processors.disqus" in TEMPLATE_CONTEXT_PROCESSORS
- DISQUS_SHORTNAME = (your shortname)

And in your template: {{ disqus }}
