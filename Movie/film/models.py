from django.db import models

# Create your models here.
class Film(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    image=models.ImageField(upload_to="film/image,null=True,blank=True")
    year=models.IntegerField()
    def __str__(self):
     return self.name