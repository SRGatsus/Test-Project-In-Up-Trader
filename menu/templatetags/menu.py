from django import template

from ..models import MenuItem

register = template.Library()

@register.inclusion_tag(filename="menu.html", takes_context=True)
def draw_menu(context,title="Menu Template"):
    request = context['request']
    if len(request.path) > 1:
        node_query = lambda x: f'''SELECT {x} FROM "menu_menuitem"
                            WHERE "menu_menuitem". "url" = '{request.path}'
                            ORDER BY "menu_menuitem". "tree_id" ASC, "menu_menuitem". "parent_id" ASC, "menu_menuitem". "lft" ASC
                            LIMIT 1'''
        menu_items_query = f'''SELECT * FROM "menu_menuitem"
            WHERE ("menu_menuitem"."lft" >=( {node_query("lft")}) AND "menu_menuitem"."rght" <= ({node_query("rght")} )
            AND "menu_menuitem"."tree_id" =( {node_query("tree_id")}))
            ORDER BY "menu_menuitem"."tree_id" ASC, "menu_menuitem"."lft" ASC'''
        menu_items = list(MenuItem.objects.raw(menu_items_query))
        # menu_items = MenuItem.objects.get_queryset_descendants(queryset=MenuItem.objects.filter(url=request.path),include_self=True)
    else:
        menu_items = MenuItem.objects.all()
    return {
        "path": request.path,
        "menu_items": menu_items,
        "title": title,
    }