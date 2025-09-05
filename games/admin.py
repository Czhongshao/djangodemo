from django.contrib import admin
from games.models import Games, GamesInfo

# Register your models here.
class GamesAdmin(admin.ModelAdmin):
    list_display = ['game_id', 'game_name']
    list_per_page = 200
    ordering = ['game_id'] # 按照id进行排列

class GamesInfoAdmin(admin.ModelAdmin):
    list_display = [
        'game_id',                 # Steam应用ID
        'game_name',               # 游戏名称
        'game_developers',         # 开发者
        'game_publishers',         # 发行商
        'game_categories',         # 分类
        'game_genres',             # 类型
        'game_required_age',       # 要求年龄
        'game_n_achievements',     # 成就数量
        'game_platforms',          # 支持平台
        'game_is_released',        # 是否发布
        'game_release_date',       # 发布日期
        'game_additional_content', # 附加内容
        'game_total_reviews',      # 总评论数
        'game_total_positive',     # 好评数
        'game_total_negative',     # 差评数
        'game_review_score',       # 评分
        'game_review_score_desc',  # 评分描述
        'game_positive_percentual',# 好评率
        'game_metacritic',         # Metacritic评分
        'game_is_free',            # 是否免费
        'game_price_initial',      # 初始价格
    ]
    list_per_page = 10
    ordering = ['game_id'] # 按照id进行排列
    list_filter = ['game_is_free']
    search_fields = ['game_name']

admin.site.site_header = 'Steam数据管理后台'
admin.site.site_title = 'Steam数据管理后台'
admin.site.index_title = 'Steam数据管理后台'

# 注册模型
admin.site.register(Games, GamesAdmin)
admin.site.register(GamesInfo, GamesInfoAdmin)
