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
            'title':'Jaegun Jung, Ph. D. - Home',
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
            'title':'Sample plots',
            'year':datetime.now().year,
        })
    )

def papers(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/papers.html',
        context_instance = RequestContext(request,
        {
            'title':'Papers and Presentations',
            'message':'As of 2/23/2015',
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
            'title':'About Jaegun',
            'message':'He is ...',
            'year':datetime.now().year,
        })
    )
