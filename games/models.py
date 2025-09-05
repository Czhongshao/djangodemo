# games/models.py 
from django.db import models

class Games(models.Model):
    game_id = models.CharField(primary_key=True, max_length=50, db_column='game_id', verbose_name='游戏ID')
    game_name = models.CharField(max_length=255, db_column='game_name', verbose_name='游戏名称')

    class Meta:
        managed = False  # 该表不进行迁移
        db_table = 'game_list'  # 指定数据库中实际的表名
        verbose_name = '游戏'
        verbose_name_plural = '游戏列表'

    def __str__(self):
        return f"[{self.game_id}] - [{self.game_name}]"


class GamesInfo(models.Model):
    game_id = models.CharField(primary_key=True, max_length=50, db_column='steam_appid', verbose_name='Steam应用ID')
    game_name = models.CharField(max_length=255, db_column='name', verbose_name='游戏名称')
    game_developers = models.TextField(db_column='developers', verbose_name='开发者')
    game_publishers = models.CharField(max_length=255, db_column='publishers', verbose_name='发行商')
    game_categories = models.TextField(db_column='categories', verbose_name='分类')
    game_genres = models.TextField(db_column='genres', verbose_name='类型')
    game_required_age = models.IntegerField(db_column='required_age', verbose_name='要求年龄')
    game_n_achievements = models.IntegerField(db_column='n_achievements', verbose_name='成就数量')
    game_platforms = models.CharField(max_length=255, db_column='platforms', verbose_name='支持平台')
    game_is_released = models.IntegerField(db_column='is_released', verbose_name='是否发布')
    game_release_date = models.CharField(max_length=255, db_column='release_date', verbose_name='发布日期')
    game_additional_content = models.TextField(db_column='additional_content', verbose_name='附加内容')
    game_total_reviews = models.IntegerField(db_column='total_reviews', verbose_name='总评论数')
    game_total_positive = models.IntegerField(db_column='total_positive', verbose_name='好评数')
    game_total_negative = models.IntegerField(db_column='total_negative', verbose_name='差评数')
    game_review_score = models.FloatField(db_column='review_score', verbose_name='评分')
    game_review_score_desc = models.CharField(max_length=255, db_column='review_score_desc', verbose_name='评分描述')
    game_positive_percentual = models.FloatField(db_column='positive_percentual', verbose_name='好评率')
    game_metacritic = models.FloatField(db_column='metacritic', verbose_name='Metacritic评分')
    game_is_free = models.IntegerField(db_column='is_free', verbose_name='是否免费')
    game_price_initial = models.FloatField(db_column='price_initial', verbose_name='初始价格')

    class Meta:
        managed = False  # 该表不进行迁移
        db_table = 'steam_games' # 数据库表名
        verbose_name = '游戏信息'
        verbose_name_plural = '游戏信息列表'

    def __str__(self):
        return f"[{self.game_id}] - {self.game_name}"

