from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from users.models import Payments
from .models import Course, Lessons
from .serializers import CourseSerializer, LessonsSerializer, PaymentsSerializer
from django_filters.rest_framework import DjangoFilterBackend


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


class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ("course", "lessons")
    ordering_fields = ("date", "payment_method")
