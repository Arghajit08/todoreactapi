from django.db import models

# Create your models here.
class Entry(models.Model):
    id=models.AutoField(primary_key=True)
    task=models.CharField(max_length=100)
    def __str__(self):
        return str("Task")+str(self.id)
