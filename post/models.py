from django.db import models
from login.models import Account

class Post(models.Model):
    writer = models.ForeignKey(Account, verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_created=True)
    content = models.TextField()
    

class Comment(models.Model):
    writer = models.ForeignKey(Account,verbose_name="작성자",on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name='게시글', on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_created=True)

        
    