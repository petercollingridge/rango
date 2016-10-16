#!/usr/bin/env python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rango.settings')

import django
django.setup()

from rango_app.models import Category, Page


def populate():
    python_cat = add_category('Python')

    add_page(
        cat=python_cat,
        title="Official Python Tutorial",
        url="http://docs.python.org/2/tutorial/"
    )

    add_page(
        cat=python_cat,
        title="How to Think like a Computer Scientist",
        url="http://www.greenteapress.com/thinkpython/"
    )

    add_page(
        cat=python_cat,
        title="Learn Python in 10 Minutes",
        url="http://www.korokithakis.net/tutorials/python/"
    )

    django_cat = add_category("Django")

    add_page(
        cat=django_cat,
        title="Official Django Tutorial",
        url="https://docs.djangoproject.com/en/1.10/intro/tutorial01/"
    )

    add_page(
        cat=django_cat,
        title="Django Rocks",
        url="http://www.djangorocks.com/"
    )

    add_page(
        cat=django_cat,
        title="How to Tango with Django",
        url="http://www.tangowithdjango.com/"
    )

    add_page(
        cat=django_cat,
        title="Full stack Python",
        url="https://www.fullstackpython.com/django.html"
    )

    add_page(
        cat=django_cat,
        title="Django Girls",
        url="https://tutorial.djangogirls.org/en/"
    )

    frame_cat = add_category("Other Frameworks")

    add_page(
        cat=frame_cat,
        title="Bottle",
        url="http://bottlepy.org/docs/dev/"
    )

    add_page(
        cat=frame_cat,
        title="Flask",
        url="http://flask.pocoo.org"
    )

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))


def add_page(cat, title, url, views=0):
    page = Page.objects.get_or_create(category=cat, title=title)[0]
    page.url = url
    page.views = views
    page.save()
    return page


def add_category(name):
    category = Category.objects.get_or_create(name=name)[0]
    return category


if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()