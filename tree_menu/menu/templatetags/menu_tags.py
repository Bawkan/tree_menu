
from menu.models import MenuItem
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    menu_items = MenuItem.objects.filter(menu__name=menu_name).select_related('parent').order_by('id')
    menu_dict = {}
    for menu_item in menu_items:
        parent = menu_items.get(id=menu_item.parent_id) if menu_item.parent_id else None
        if parent:
            if parent.id not in menu_dict:
                menu_dict[parent.id] = {'menu_items': []}
            menu_dict[parent.id]['menu_items'].append(menu_item)
        else:
            menu_dict[menu_item.id] = {'menu_item': menu_item, 'menu_items': []}

    def recursive_draw(result, data):
        for d in data:
            item = {
                'name': d['menu_item'].name,
                'url': d['menu_item'].url,
                'is_active': request.path.startswith(d['menu_item'].url) if d['menu_item'].url else False,
                'children': [],
            }
            recursive_draw(item['children'], d['menu_items'])
            result.append(item)

    result = []
    recursive_draw(result, list(menu_dict.values()))
    return result
