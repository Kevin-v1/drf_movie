from django.db import models 
from django.contrib.auth.models import User

from shortuuidfield import ShortUUIDField
from movie.models import Movie


class Profile(models.Model):
    """
    用户信息类
    """
    UNVERIFIED = 0
    ACTIVATED = 1
    DISABLED = 2
    DELETED = 3

    USER_STATUS = (
        (UNVERIFIED, u'未验证'),
        (ACTIVATED, u'已激活'),
        (DISABLED, u'已禁用'),
        (DELETED, u'已删除'),
    )

    uid = ShortUUIDField(max_length=32, primary_key=True, unique=True, verbose_name='用户唯一标识')
    # phone = models.CharField(max_length=11, blank=True, null=True, verbose_name='用户电话', db_index=True)
    # email = models.CharField(max_length=40, blank=True, null=True, verbose_name='用户邮箱', db_index=True)
    # avatar = models.CharField(max_length=60, blank=True, null=True, verbose_name='用户头像')

    # 会员相关
    is_upgrade = models.IntegerField(default=0, verbose_name='是否升级会员')
    upgrade_time = models.DateTimeField(blank=True, null=True, verbose_name='升级日期')
    expire_time = models.DateTimeField(blank=True, null=True, verbose_name='过期时间')
    upgrade_count = models.IntegerField(default=0, verbose_name='升级次数')
    # 关联用户表
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 新增
    movies = models.ManyToManyField(Movie)

    class Meta:
        db_table = 'profile'
        verbose_name = '用户信息'
        verbose_name_plural = '用户信息'
