from rest_framework import serializers
from dogs.models import Dog, Breed #, LANGUAGE_CHOICES, STYLE_CHOICES
from django.core.validators import MinValueValidator, MaxValueValidator

#previously class DogSerializer(serializers.ModelSerializer):
class DogSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    age = serializers.IntegerField()
    breed = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    gender = serializers.CharField(max_length=2)
    color = serializers.CharField(max_length=30)
    favoritefood = serializers.CharField(max_length=30)
    favoritetoy = serializers.CharField(max_length=30)
    
    class Meta:
        model = Breed
        fields = ['name', 'size', 'friendliness', 'trainability', 'sheddingamount', 'exerciseneeds']
        #fields = ['name', 'age', 'breed', 'gender', 'color', 'favoritefood', 'favoritetoy']
        # Previously put info comment out for test['id', 'title', 'code', 'linenos', 'language', 'style']

    def create(self, validated_data):
        """
        Create and return a new `Dog` instance, given the validated data.
        """
        return Dog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Dog` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.breed = validated_data.get('breed', instance.breed)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.color = validated_data.get('color', instance.color)
        instance.favoritefood = validated_data.get('favoritefood', instance.favoritefood)
        instance.favoritetoy = validated_data.get('favoritetoy', instance.favoritetoy)
        instance.save()
        return instance
        
class BreedSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    size = serializers.CharField(max_length=2)
    friendliness = serializers.IntegerField()
    trainability = serializers.IntegerField()
    sheddingamount = serializers.IntegerField()
    exerciseneeds = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Breed` instance, given the validated data.
        """
        return Breed.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Breed` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.size = validated_data.get('size', instance.size)
        instance.friendliness = validated_data.get('friendliness', instance.friendliness)
        instance.trainability = validated_data.get('trainability', instance.trainability)
        instance.sheddingamount = validated_data.get('sheddingamount', instance.sheddingamount)
        instance.exerciseneeds = validated_data.get('exerciseneeds', instance.exerciseneeds)
        instance.save()
        return instance