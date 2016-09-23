# coding=utf-8
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
  avatar = models.ImageField(upload_to='doctor/%Y/%m', default='avatar/default.png', max_length=200, blank=True, null=True, verbose_name='医生头像')
  DOCTOR_LEVEL = (
    ('level1', '住院医师'),
    ('level2', '主治医师'),
    ('level3', '副主任医师'),
    ('level4', '主任医师'),
  )
  level = models.CharField(max_length=7, verbose_name='医生职称', choices=DOCTOR_LEVEL, default='level1')
  introduce = models.TextField(verbose_name='医生介绍')
  hospital = models.ForeignKey('Hospital', verbose_name='所属医院')

  class Meta:
    verbose_name = '医生'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.name

class Comment(models.Model):
  content = models.TextField(verbose_name='评论内容')
  create_at = models.DateField(auto_now_add=True, verbose_name='评论时间')
  doctor = models.ForeignKey('Doctor', verbose_name='医生')
  pid = models.ForeignKey('self', blank=True, null=True, verbose_name='父级评论')
  praise_count = models.IntegerField(default=0, verbose_name='点赞人数')
  ATTITUDE_CHOICE = (
    ('bad', '坏'),
    ('well', '一般'),
    ('good', '好'),
    ('better', '很好'),
  )
  attitude = models.CharField(choices=ATTITUDE_CHOICE, default='good', verbose_name='医生态度', max_length=10)
  duration = models.IntegerField(verbose_name='诊疗时长', default=10)

  class Meta:
    verbose_name = '评论'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.content
