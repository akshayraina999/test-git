from django.db import models

# Create your models here.


class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eemail = models.EmailField()  
    econtact = models.CharField(max_length=15)

    class Meta:  
        db_table = "employee"


class Posts(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=350)
    category = models.CharField(max_length=50)
    blog_id = models.CharField(max_length=50)

    class Meta:
        db_table = "posts"


