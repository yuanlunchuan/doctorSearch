from __future__ import unicode_literals

from django.db import models

class DiseaseCategory(models.Model):
  name = models.CharField(max_length=20, verbose_name='分类名称')
  pid = models.ForeignKey('self', blank=True, null=True, verbose_name='上一级分类')

  class Meta:
    verbose_name = '疾病分类'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.name

class Disease(models.Model):
  name = models.CharField(max_length=20, verbose_name='疾病名称')
  desc = models.TextField(verbose_name='疾病介绍')
  category = models.ForeignKey(DiseaseCategory, verbose_name='分类', default="")

  class Meta:
    verbose_name = '疾病'
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.name
