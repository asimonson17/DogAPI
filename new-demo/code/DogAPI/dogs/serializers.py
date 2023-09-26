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
        #instance.title = validated_data.get('title', instance.title)
        #instance.code = validated_data.get('code', instance.code)
        #instance.linenos = validated_data.get('linenos', instance.linenos)
        #instance.language = validated_data.get('language', instance.language)
        #instance.style = validated_data.get('style', instance.style)
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.breed = validated_data.get('breed', instance.breed)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.color = validated_data.get('color', instance.color)
        instance.favoritefood = validated_data.get('favoritefood', instance.favoritefood)
        instance.favoritetoy = validated_data.get('favoritetoy', instance.favoritetoy)
        instance.save()
        return instance
        
