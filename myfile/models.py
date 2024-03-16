from django.db import models

class Uploads(models.Model):
        title=models.CharField(max_length=50)
        file = models.FileField(upload_to='file/' )
        
        
