

from django.db import models

# Create your models here.



def validate_for_a(Svalue):
    if Svalue[0].lower()=='a':
        raise models.ValidationError("First letter should not be a")

def validate_for_len(name):
    if len(name)<=5:
        raise models.ValidationError('len is less than 5')


class Topic(models.Model):
    topic_name=models.CharField(max_length=100)
    def __str__(self):
        return self.topic_name


    
class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,validators=[validate_for_a,validate_for_len])
    url=models.URLField()
    def __str__(self):
        return self.name



class AccessRecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=20)

    def __str__(self):
        return self.author
