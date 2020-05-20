from django.db import models

# Create your models here

class Book(models.Model):
    CHOISE = (('EN','English'),('HD','Hindhi'))
    book_name = models.CharField(null=True,blank=True,max_length=255)
    pages = models.IntegerField(null=True,blank=True)
    prcie = models.FloatField(null=True,blank=True)
    language = models.CharField(null=True,blank=True,choices=CHOISE,max_length=255)
    book = models.FileField(blank=True, null=True)
    date_published= models.DateTimeField(auto_now_add=True)
    date_reviewed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.book_name

class Publications(models.Model):
    publications_name=models.CharField(null=True,blank=True,max_length=255)
    address = models.CharField(null=True,blank=True,max_length=550)
    city = models.CharField(null=True,blank=True,max_length=255)
    zip_code = models.IntegerField(null=True,blank=True)
    phone_no = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.publications_name

class Author(models.Model):
    name = models.CharField(null=True,blank=True,max_length=255)
    email = models.EmailField(null=True,blank=True,max_length=255)
    phone_no = models.IntegerField(null=True,blank=True)
    book = models.ForeignKey(Book,on_delete=models.CASCADE,blank=True, null=True)
    publications = models.ManyToManyField(Publications)

    def __str__(self):
        return self.name

