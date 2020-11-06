from django.db import models

# Create your models here.

class Pizza(models.Model):
	CRUST_CHOICES = [
        ('CB', 'cheese burst'),
        ('CHT', 'classic hand tossed'),
        ('WTC', 'wheat thin crust'),
        ('FPP', 'fresh pan pizza'),
        ('NHT', 'new hand tossed'),
    ]
	name=models.CharField(max_length=50, blank=False, default='')
	small_or_large=models.BooleanField(default=False)
	price=models.IntegerField(blank=False)
	crust=models.CharField(choices=CRUST_CHOICES, default='FPP', max_length=50)
	veg_nonveg=models.BooleanField(default=False)

