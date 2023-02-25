from rest_framework import serializers
from .models import RatingChoices
from .models import Movie, MovieOrder
from users.serializer import UserSerializer


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default=None)
    rating = serializers.ChoiceField(choices=RatingChoices.choices, default="G")
    synopsis = serializers.CharField(default=None)
    added_by = serializers.CharField(default=None)

    def create(self, validated_data: dict) -> Movie:
        
        return Movie.objects.create(**validated_data)
    
class MovieOrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    price = serializers.DecimalField(max_digits=8, decimal_places=2)
    buyed_at = serializers.DateTimeField(read_only=True)
    buyed_by = serializers.CharField()
    title = serializers.CharField()



    def create(self, validated_data: dict) -> Movie:
        
        return MovieOrder.objects.create(**validated_data)


    
