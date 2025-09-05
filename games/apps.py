from django.apps import AppConfig


class GamesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'games'
    # 更改app名称
    verbose_name = '游戏列表'
