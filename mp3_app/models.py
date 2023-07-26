from django.db import models
from django.contrib.auth.models import User
 
class allsongs(models.Model):
    song_id=models.AutoField(primary_key=True)
    song_title=models.TextField()
    song_category=models.CharField(max_length=50)
    song_file=models.FileField(upload_to='songs/')
    
    def __str__(self):
        return self.song_title
    
class Favourites(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    song=models.ForeignKey(allsongs,on_delete=models.CASCADE)  
    def __str__(self):
        return self.user.username


     
# Create your models here.
