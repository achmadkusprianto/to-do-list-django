from django.db import models

'''
    tahap 1 dari semua tahap memasukkan database, 
    tahap 2 = python manage.py makemigrations
    tahap 3 = python manage.py migrate
'''

class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False) #tidak usah diisi karena nilai defaultnya ada

    def __str__(self):
        return self.item + ' | ' + str(self.completed)
