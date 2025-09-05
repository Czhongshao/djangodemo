# games/views.py
from django.core.paginator import Paginator
from django.http import JsonResponse
from games.models import Games, GamesInfo

def gamesAPI(request):
    game_id   = request.GET.get('game_id')
    game_name = request.GET.get('game_name')

    queryset = Games.objects.all()
    if game_id:
        queryset = queryset.filter(game_id=game_id)
    if game_name:
        queryset = queryset.filter(game_name__icontains=game_name)

    try:
        page = int(request.GET.get('page', 1))
        if page < 1:
            page = 1
    except ValueError:
        page = 1

    try:
        page_size = int(request.GET.get('page_size', 1000))
        if page_size > 1000 or page_size < 1:
            page_size = 1000
    except ValueError:
        page_size = 1000

    paginator = Paginator(queryset.values('game_id', 'game_name'), page_size)
    page_obj  = paginator.get_page(page)

    return JsonResponse(
        {
            'page':       page,
            'page_size':  page_size,
            'total':      paginator.count,
            'total_page': paginator.num_pages,
            'data':       list(page_obj)
        },
        safe=False,
        json_dumps_params={'ensure_ascii': False}
    )

def gamesInfoAPI(request):
    game_id = request.GET.get('game_id')
    queryset = GamesInfo.objects.all()
    if game_id:
        queryset = queryset.filter(game_id=game_id)
    else:
        queryset = queryset.filter(game_id__in=Games.objects.all().values_list('game_id', flat=True))
    queryset = queryset.values()
    return JsonResponse(
        {
            'total':      queryset.count(),
            'data':       list(queryset)
        },
        safe=False,
        json_dumps_params={'ensure_ascii': False}
    )