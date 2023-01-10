from django.template import Library
from ..models import Category


register = Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context: dict, menu: str) -> dict:

    try:
        categories = Category.objects.filter(menu__title=menu)
        cat_values = categories.values()
        first_cat = [cat for cat in cat_values.filter(parent=None)]
        selected_cat_id = int(context['request'].GET[menu])
        selected_cat = categories.get(pk=selected_cat_id)
        selected_cat_id_list = get_selected_cat_id_list(selected_cat, first_cat, selected_cat_id)

        for cat in first_cat:
            if cat['id'] in selected_cat_id_list:
                cat['child_cats'] = get_child_cats(cat_values, cat['id'], selected_cat_id_list)
        dict_to_return = {'cats': first_cat}

    except:
        selected_cat_id = None
        dict_to_return = {
            'cats': [
                cat for cat in Category.objects.filter(menu__title=menu, parent=None).values()
            ]
        }

    dict_to_return['menu'] = menu
    dict_to_return['selected_cat_id'] = selected_cat_id
    dict_to_return['query'] = get_query(context, menu)

    return dict_to_return


def get_selected_cat_id_list(selected_cat, first_cat: list, selected_cat_id: int) -> list:
    selected_cat_id_list = []

    while selected_cat:
        selected_cat_id_list.append(selected_cat.id)
        selected_cat = selected_cat.parent
    if not selected_cat_id_list:
        for cat in first_cat:
            if cat['id'] == selected_cat_id:
                selected_cat_id_list.append(selected_cat_id)
    return selected_cat_id_list


def get_child_cats(cat_values, cat_id: int, selected_cat_id_list: list) -> list:
    cat_list = [cat for cat in cat_values.filter(parent_id=cat_id)]
    for cat in cat_list:
        if cat['id'] in selected_cat_id_list:
            cat['child_cats'] = get_child_cats(cat_values, cat['id'], selected_cat_id_list)
    return cat_list


def get_query(context: dict, menu: str) -> str:
    args = []
    for arg in context['request'].GET:
        if arg != menu:
            args.append('='.join((arg, context['request'].GET[arg])))
    query = '&'.join(args)
    return query

