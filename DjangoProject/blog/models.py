from django.db import models

# Create your models here.
class Post(models.Model):
    # 50자 까지 가능하다
    title = models.CharField(max_length=50)
    content = models.TextField()
    
    # 시간을 저장하는기능
    created_at = models.DateTimeField()
    # author 