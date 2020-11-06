from rest_framework import serializers 
from api.models import Pizza
 
 
class PizzaSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Pizza
        fields = ('id',
                  'name',
                  'small_or_large',
                  'price',
                  'crust',
                  'veg_nonveg')