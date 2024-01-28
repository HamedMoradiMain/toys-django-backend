from django.db import models
class Toys(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100,blank=True,null=True)
    toy_category = models.ForeignKey('toyCategory',on_delete=models.CASCADE)
    release_date = models.DateTimeField()
    was_included_in_home = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class toyCategory(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "toyCategories"
    def __str__(self):
        return self.name