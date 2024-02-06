from django import template

register = template.Library()

@register.inclusion_tag(filename="menu.html", takes_context=True)
def draw_menu(context,title="Menu Template"):
    return {
        "title":title
    }