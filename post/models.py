from django.db import models
from auth.models import Account

class Post(models.Model):
    writer = models.ForeignKey(Account, verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_created=True)
    content = models.TextField()
    __str__(self):
        return self.title
    

class Comment(models.Model):
    writer = models.ForeignKey(Account,verbose_name="작성자",on_delete)
    post = models.ForeignKey(Post, verbose_name='게시글', on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_created=True)
    __str__(self):
        return self.pub_date
        
    