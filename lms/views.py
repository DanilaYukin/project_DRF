from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsModer, IsOwner
from .models import Course, Lessons
from .serializers import CourseSerializer, LessonsSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [~IsModer]
        elif self.action == 'destroy':
            self.permission_classes = [~IsModer]
        elif self.action == 'update':
            self.permission_classes = [IsModer | IsOwner]
        elif self.action == 'retrieve':
            self.permission_classes = [IsModer | IsOwner]
        elif self.action == 'list':
            self.permission_classes = [IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [~IsModer]

    def perform_create(self, serializer):
        lesson = serializer.save()
        lesson.owner = self.request.user
        lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsModer | IsOwner]


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsModer | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonsSerializer
    permission_classes = [IsModer | IsOwner]


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [~IsModer | IsOwner]
