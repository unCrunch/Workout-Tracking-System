from rest_framework import serializers

from .models import Exercise, Workout

class ExerciseSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    exercise_type = serializers.ChoiceField(choices=Exercise.EXERCISE_TYPES)
    
    def create(self, validated_data):
        return Exercise.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.exercise_type = validated_data.get ('exercise_type', instance.exercise_type)
        instance.save()
        return instance
    
class WorkoutSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Workout
        fields = '__all__'