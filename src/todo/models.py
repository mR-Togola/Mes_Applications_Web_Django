from django.db import models
from django.utils.text import slugify

# Create your models here.


class Collection(models.Model):
    nom = models.CharField(max_length=60)
    slug = models.SlugField()
    
    
    @classmethod
    def get_default_collection(cls):
       collecton, _ =  cls.objects.get_or_create(nom="Défaut", slug="_defaut")
       return collecton
   
    def __str__(self):
        return self.nom
    
    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.nom)
        super().save(*args, **kwargs)
    

class Taches(models.Model):
    description = models.CharField(max_length=300)
    collection = models.ForeignKey(Collection,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.description