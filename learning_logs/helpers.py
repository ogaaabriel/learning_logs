from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def paginate(request, obj_list, per_page=10):
    page = request.GET.get("pagina", 1)
    paginator = Paginator(obj_list, per_page)

    try:
        obj_list = paginator.page(page)
    except PageNotAnInteger:
        obj_list = paginator.page(1)
    except EmptyPage:
        obj_list = paginator.page(paginator.num_pages)

    return obj_list


def search_topics(search, topics_list):
    return topics_list.filter(Q(title__istartswith=search))
