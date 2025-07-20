from rest_framework import viewsets, generics

from .models import Course, Lessons
from .serializers import CourseSerializer, LessonsSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonsSerializer


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonsSerializer
