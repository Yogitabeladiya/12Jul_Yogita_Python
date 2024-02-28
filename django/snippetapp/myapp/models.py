from django.db import models

# Create your models here.
language=(
  ('pyton','pyhton'),
  ('java','java'),
  ('javascript','javascript'),
  ('c','c'),
  ('c++','c++'),
  ('c#','c#'),
  ('asp.net','asp.net')
)

styles=(
    ('friendly','friendly'),
    ('defaut','default')
)

catagaroy_Choices=(
    ('m','mobaile'),
    ('l','laptop'),
    ('tw','topware'),
    ('bw','botware')
)

class snippest(models.Model):
    title=models.CharField(max_length=50)
    code=models.TextField()
    linenos=models.BooleanField(default=False)
    language=models.CharField(choices=language, max_length=50)
    style=models.CharField(choices=styles,max_length=30)






