from django.db import models

class Hospital(models.Model):
  name = models.CharField(max_length=20, verbose_name='医院')
  address = models.CharField(max_length=30, verbose_name='地址')
  map_link = models.URLField(verbose_name='地图链接')
  profile = models.TextField(verbose_name='医院简介')
  introduction = models.TextField(verbose_name='医院介绍')
  image = models.ImageField(upload_to='hospital/%Y/%m', default='hospital/default.png', max_length=200, blank=True, null=True, verbose_name='医院图片')

  class Meta:
    verbose_name = '医院'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.name

class Doctor(models.Model):
  name = models.CharField(max_length=10, verbose_name='姓名')
