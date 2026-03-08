from django import template
from django.urls import resolve

register = template.Library()

@register.simple_tag(takes_context=True)
def active_link(context, url_name, active_classes, inactive_classes):
    request = context.get("request")
    if not request:
        return inactive_classes

    try:
        current_url_name = resolve(request.path_info).url_name
        if current_url_name == url_name:
            return active_classes
    except:
        pass
    return inactive_classes

@register.filter
def tech_badge_style(tech_name):
    mapping = {
        'Python': 'bg-blue-100 text-blue-700 border-blue-200',
        'Django': 'bg-green-100 text-green-700 border-green-200',
        'Tailwind': 'bg-sky-100 text-sky-700 border-sky-200',
        'JavaScript': 'bg-yellow-100 text-yellow-700 border-yellow-200',
        'PostgreSQL': 'bg-indigo-100 text-indigo-700 border-indigo-200',
        'SQLite': 'bg-slate-100 text-slate-700 border-slate-200',
    }

    return mapping.get(tech_name, 'bg-gray-100 text-gray-700 border-gray-200')