from rest_framework import serializers
from .models import Toys
class ToySerializer(serializers.ModelSerializer):
    class Meta:
        model = Toys
        fields = ('id','name','description','toy_category','release_date','was_included_in_home','created')