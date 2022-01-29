from rest_framework import serializers
from .models import Products


class ProductsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'

    def validate(self, attrs):
        if len(attrs['name']) < 4:
            raise serializers.ValidationError({
                'name': 'Must be at least 4 character long'
            })
