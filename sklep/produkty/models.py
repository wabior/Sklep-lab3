from django.db import models

class Producent(models.Model):
    def __str__(self):
        return self.nazwa
    nazwa   = models.CharField(max_length=60)
    opis    = models.TextField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = "Producent"
        verbose_name_plural = "Producenci"

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=30)
    def __str__(self):
        return self.nazwa
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = "Kategria"
        verbose_name_plural = "Kategrie"

class Tagi(models.Model):
    def __str__(self):
        return self.name
    name    = models.CharField(max_length=40)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = "Tag"
        verbose_name_plural = "Tagi"

class Produkty(models.Model):
    def __str__(self):
        return self.nazwa
    nazwa   = models.CharField(max_length=60)
    opis    = models.TextField(blank=True)
    cena    = models.DecimalField(max_digits=99999 ,decimal_places=2)
    producent = models.ForeignKey(Producent,on_delete=models.CASCADE,blank=True,null=True)
    kategoria = models.ForeignKey(Kategoria,on_delete=models.CASCADE,blank=True,null=True)
   # komentaż  = models.ForeignKey(Comment,on_delete=models.CASCADE,blank=True,null=True)
    tagi      = models.ManyToManyField(Tagi,blank=True,null=True)
    obraz   = models.FileField(upload_to='', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = "Produkt"
        verbose_name_plural = "Produkty"

class Comment(models.Model):
    def __str__(self):
        return self.user_adent
    produkt = models.ForeignKey(Produkty,on_delete=models.CASCADE,blank=True)
    content = models.TextField()
    ip      = models.GenericIPAddressField()
    user_adent = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = "Komentaż"
        verbose_name_plural = "Komentaże"