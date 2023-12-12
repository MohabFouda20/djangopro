from django.db import models

# Create your models here.

class rooms(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    phoneNumber = models.CharField(max_length=12)
    created_date = models.DateTimeField( auto_now_add=True ) #make time and date auto at first time time
    created_update = models.DateTimeField(auto_now= True) #add every time
    
    
    def __str__(self):
        return str(self.name)