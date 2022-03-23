from django.db import models
from django.contrib.auth import get_user_model

class DuckModel(models.Model):
  owner         = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  title         = models.CharField(max_length=60)
  details       = models.TextField(default='')
  create_date   = models.DateTimeField(auto_now_add=True)
  updated_date  = models.DateTimeField(auto_now=True)


  def __str__(self):
    return self.create_date, self.title



