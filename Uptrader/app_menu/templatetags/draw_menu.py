from django import template
from ..models import Category
from django.db import connection, reset_queries

register = template.Library()


@register.inclusion_tag('menu/draw_menu.html', takes_context=True)
def draw_menu(context: dict, menu: str) -> dict:
    """Тэг шаблона возвращающий вложенное меню."""
    dict_to_return = dict()
    reset_queries()
    path = ""
    depth = 0
    try:

        selected_category_id = int(context['request'].GET[menu])
        categories = list(Category.objects.select_related("menu").filter(menu__title=menu).values())
        for category in categories:
            if category['id'] == selected_category_id:
                path = category['path']
                depth = category['depth']

    except KeyError:
        categories = list(Category.objects.select_related("menu").filter(menu__title=menu)\
                          .filter(depth=0).order_by('path').values())

    dict_to_return['queryset'] = categories
    dict_to_return['depth'] = depth
    dict_to_return['path'] = path
    dict_to_return['menu'] = menu
    dict_to_return['query'] = get_query(context, menu)
    print(len(connection.queries))
    return dict_to_return


@register.simple_tag
def get_level_elements(path, queryset, current_depth) -> list:
    """Тег для получения элементов определенного уровня глубины."""
    elements_list = []
    for query in queryset:
        if query["path"].startswith(path[:current_depth*2]) and query['depth'] == current_depth:
            elements_list.append(query)
    print(len(connection.queries))
    return elements_list


@register.filter
def starts_with(value, arg):
    """Фильтр проверяющий строки на совпадения."""
    if value.startswith(arg):
        return True
    return False


def get_query(context: dict, menu: str) -> str:
    """Возвращает аргументы url."""
    args = []
    for arg in context['request'].GET:
        if arg != menu:
            args.append('='.join((arg, context['request'].GET[arg])))
    query = '&'.join(args)
    return query

