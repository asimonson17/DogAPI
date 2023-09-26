from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
#from pygments.lexers import get_all_lexers
#from pygments.styles import get_all_styles

#LEXERS = [item for item in get_all_lexers() if item[1]]
#LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
#STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Dog(models.Model):
    name = models.CharField(max_length=30, null=True, blank=False)
    age = models.IntegerField(validators=[
            MinValueValidator(0),
            MaxValueValidator(99)], null=True, blank=False)
    breed = models.ForeignKey('dogs.breed', on_delete=models.CASCADE,
        )
    FEMALE = "FM"
    MALE = "ML"
    GENDER_CHOICES = [
        (FEMALE, "Female"),
        (MALE, "Male"),
        ]
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default=MALE)
    color = models.CharField(max_length=30, null=True, blank=False)
    favoritefood = models.CharField(max_length=30, null=True, blank=False)
    favoritetoy = models.CharField(max_length=30, null=True, blank=False)
    #linenos = models.BooleanField(default=False)
    #language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    #style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    
    
class Breed(models.Model):
    name = models.CharField(max_length=40, null=True, blank=False)
    TINY = "TY"
    SMALL = "SM"
    MEDIUM = "MD"
    LARGE = "LG"
    BREED_SIZE_CHOICES = [
        (TINY, "Tiny"),
        (SMALL, "Small"),
        (MEDIUM, "Medium"),
        (LARGE, "Large"),
    ]
    size = models.CharField(max_length=2, choices=BREED_SIZE_CHOICES, default=MEDIUM)
    friendliness = models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(5)])
    trainability = models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(5)])
    sheddingamount = models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(5)])
    exerciseneeds = models.IntegerField(validators=[
            MinValueValidator(1),
            MaxValueValidator(5)])
    pass


