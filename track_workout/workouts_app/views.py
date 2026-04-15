from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import ExerciseSerializer, WorkoutSerializer
from .models import Exercise, Workout

# Create your views here.
class ExerciseAPIView(APIView):
    def get(self, request, id=None):
        if id:
            exercise = get_object_or_404(Exercise, id=id)
            serializer = ExerciseSerializer(exercise)
            return Response(serializer.data)
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ExerciseSerializer(data=request.data)
        if serializer.is_valid():
            exercise = serializer.save()
            return Response(ExerciseSerializer(exercise).data, status=201)
        return Response(serializer.errors, status=400)
    
    def put(self, request, id):
        return self.update(request, id, partial=False)
    def patch(self, request, id):
        return self.update(request, id, partial=True)
    
    def update(self, request, id, partial=False):
        exercise = get_object_or_404(Exercise, id=id)
        serializer = ExerciseSerializer(exercise, data=request.data, partial=partial)
        if serializer.is_valid():
            exercise = serializer.save()
            return Response(ExerciseSerializer(exercise).data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, id):
        exercise = get_object_or_404(Exercise, id=id)
        exercise.delete()
        return Response(status=204)

class WorkoutViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] 
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer