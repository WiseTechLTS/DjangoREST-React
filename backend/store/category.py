from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=55)
    # @staticmethod is a decorator that allows us to call the method without creating an instance of the class
    @staticmethod
    # get_all_categories() is a method that returns all the categories in the database
    def get_all_categories():
        return Category.objects.all()
    
    # __str__ is a method that returns the name of the category
    def __str__(self):
        return self.name