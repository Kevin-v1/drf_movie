from django.db import models

# 地区
Region = [
    (1,'中国大陆'),
    (2,'中国香港'),
    (3,'中国台湾'),
    (4,'美国'),
    (5,'韩国'),
    (6,'日本'),
    (7,'其他')
]
# 清晰度
Quality = [
    (1, '720P'),
    (2, '1080P'),
    (3, '4K')
]

# 热门精选
Hot = [
    (False,'否'),
    (True,'是')
]
# 置顶
Top = [
    (False,'否'),
    (True,'是')
]
# 是否限制
SHOW = [
    (False, '否'),
    (True, '是')
]
# 是否免费
FREE = [
    (False, '否'),
    (True, '是')
]

class Category(models.Model):
    # 分类信息
    id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=100, verbose_name="分类名")

    class Meta:
        db_table = "category" # 指定数据库表名
        verbose_name = "分类管理"
        verbose_name_plural = "分类管理"

    def __str__(self):
        return self.category_name

class Movie(models.Model):
    # 电影信息
    id = models.AutoField(primary_key=True)
    movie_name = models.CharField(max_length=100,verbose_name='电影名')
    release_year = models.IntegerField(verbose_name='上映年份')
    director = models.CharField(max_length=100,verbose_name='导演')
    scriptwriter = models.CharField(max_length=100,verbose_name='编剧')
    actors = models.CharField(max_length=200,verbose_name='主演')
    region = models.SmallIntegerField(choices=Region,verbose_name='地区')
    types = models.CharField(max_length=50,verbose_name='类型')
    language = models.CharField(max_length=100,verbose_name='语言')
    release_date = models.DateField(verbose_name='上映日期')
    duration = models.CharField(max_length=50,verbose_name='时长(或集数)')
    alternate_name = models.CharField(max_length=100,blank=True,verbose_name='又名')
    image_url = models.CharField(max_length=300,blank=True,verbose_name='图片链接')
    rate = models.FloatField(blank=True,verbose_name='豆瓣评分')
    review = models.TextField(max_length=500,blank=True,verbose_name='简介')
    is_hot = models.BooleanField(choices=Hot,default=False,verbose_name='是否热门')
    is_top = models.BooleanField(choices=Top,default=False,verbose_name='是否置顶')
    quality = models.SmallIntegerField(choices=Quality,blank=False,verbose_name='清晰度')
    subtitle = models.CharField(max_length=100,blank=True,verbose_name='字幕')
    update_info = models.CharField(max_length=100,blank=True,verbose_name='更新信息')
    update_progress = models.CharField(max_length=100,blank=True,verbose_name='更新进度')
    download_info = models.TextField(max_length=500,blank=True,verbose_name='网盘信息',
                                     help_text="每个网盘信息占一行，每个字段用网盘名:网址 提取码:字符 组成（无提取码不写）。 如 百度网盘:http://www.baidu.com  提取码:8888 ")
    is_show = models.BooleanField(choices=SHOW,default=True,verbose_name='是否显示')
    is_free = models.BooleanField(choices=FREE,default=False,verbose_name='是否免费')
    # 设置外键关联
    category = models.ForeignKey(Category,blank=False,verbose_name='分类名', on_delete=models.CASCADE) 



    class Meta:
        db_table = 'movie'
        verbose_name = '电影管理'
        verbose_name_plural = '电影管理'

    def __str__(self):
        return self.movie_name