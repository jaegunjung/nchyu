# -*- coding: utf-8 -*-
"""
Definition of views.
"""
import json
import os

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.conf import settings
from django.http import Http404
from django.template import Template, Context
from django.template.loader_tags import BlockNode
from django.utils._os import safe_join
from django.views.generic import ListView, DetailView
from .models import Post


def get_page_or_404(name):
    """Return page content as a Django template or raise 404 error."""
    try:
        file_path = safe_join(settings.SITE_PAGES_DIRECTORY, name)
    except ValueError:
        raise Http404('Page Not Found')
    else:
        if not os.path.exists(file_path):
            raise Http404('Page Not Found')
   
    with open(file_path, 'r') as f:
        page = Template(f.read())
    meta = None
    for i, node in enumerate(list(page.nodelist)):
        if isinstance(node, BlockNode) and node.name == 'context':
            meta = page.nodelist.pop(i)
            break
    page._meta = meta
    return page


def page(request, slug='index'):
    """Render the requested page if found."""
    file_name = '{}.html'.format(slug)
    page = get_page_or_404(file_name)
    context = {
        'slug': slug,
        'page': page,
    }
    if page._meta is not None:
        meta = page._meta.render(Context())
        extra_context = json.loads(meta)
        context.update(extra_context)
    return render(request, 'page.html', context)

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )

def mentors(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/mentors.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )

def yearend(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/yearend.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )

def organization(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/organization.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )

def figures(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/figures.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )

def g_photos(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/g_photos.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )

def g_videos(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/g_videos.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )

def events(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/events.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )

def googled6ad0f10bcbda8f2(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/googled6ad0f10bcbda8f2.html',
        context_instance = RequestContext(request,
        {
            'year':datetime.now().year,
        })
    )
"""
def post_list(request):
    return render(request, 'app/post_list.html')
"""

post_list = ListView.as_view(model=Post)
print('post_list')
print(post_list)


post_detail = DetailView.as_view(model=Post)
