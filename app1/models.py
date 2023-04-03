from django.db import models

# Create your models here.
class Hari(models.Model):
    h_name=models.CharField(max_length=100,primary_key=True)
    def__str__(self):
        return self.topic_name

class webpage(models.Model):
    h_name=models.ForeignKey(Hari,on_delete=models.CASCADE)
    name=models.CharFeild(max_length=100)
    urls=models.URLFeild()
class accessreads(models.Model):
    name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return self.date

