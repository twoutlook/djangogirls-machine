from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    # brief = models.CharField(default='', max_length=200)
    # text = models.CharField(default='', max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

   
    r01c4=models.CharField(default='', max_length=99)
    r01c6=models.CharField(default='', max_length=99)
    r01c8=models.CharField(default='', max_length=99)
   
   
    #
    r03c3=models.CharField(default='', max_length=99)
    r03c4=models.CharField(default='', max_length=99)
    r03c5=models.CharField(default='', max_length=99)
    r03c6=models.CharField(default='', max_length=99)
    r03c7=models.CharField(default='', max_length=99)

    r04c3=models.CharField(default='', max_length=99)
    r04c4=models.CharField(default='', max_length=99)
    r04c5=models.CharField(default='', max_length=99)
    r04c6=models.CharField(default='', max_length=99)
    r04c7=models.CharField(default='', max_length=99)

          
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title