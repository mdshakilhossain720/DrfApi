
from .models import Carlist
from rest_framework import serializers

class CarlistSerializer(serializers.ModelSerializer):
    discount_prices=serializers.SerializerMethodField()
    class Meta:
        model = Carlist
        fields = '__all__'

    def get_discount_prices(self, object):
        discountprices = object.prices-5000
        return discountprices

# class CarlistSerializer(serializers.Serializer):
   
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    des = serializers.CharField(max_length=100)
    active = serializers.BooleanField(default=True)
    color = serializers.CharField(max_length=100)   

    def create(self, validated_data):
        return Carlist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.des = validated_data.get('des', instance.des)
        instance.active = validated_data.get('active', instance.active)
        instance.color = validated_data.get('color', instance.color)
        instance.save()
        return instance

    