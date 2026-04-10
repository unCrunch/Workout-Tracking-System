from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ExerciseSerializer
from .models import Exercise

# Create your views here.
class ExerciseAPIView(APIView):
    def get(self, request):
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data)
        