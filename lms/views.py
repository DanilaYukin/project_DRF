from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from users.permissions import IsModer, IsOwner
from .models import Course, Lessons, Subscription
from .paginators import LMSPaginator
from .serializers import CourseSerializer, LessonsSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = LMSPaginator

    def get_permissions(self):
        if self.action == "create":
            self.permission_classes = [~IsModer]
        elif self.action == "destroy":
            self.permission_classes = [~IsModer]
        elif self.action == "update":
            self.permission_classes = [IsModer | IsOwner]
        elif self.action == "retrieve":
            self.permission_classes = [IsModer | IsOwner]
        elif self.action == "list":
            self.permission_classes = [IsOwner]
        return [permission() for permission in self.permission_classes]

    def perform_create(self, serializer):
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


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
    pagination_class = LMSPaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [IsModer | IsOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonsSerializer
    permission_classes = [IsModer | IsOwner]
    queryset = Lessons.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    serializer_class = LessonsSerializer
    queryset = Lessons.objects.all()
    permission_classes = [~IsModer | IsOwner]


class SubscriptionAPIView(APIView):

    @staticmethod
    def post(request, *args, **kwargs):
        user = request.user
        course_id = request.data.get("course_id")

        if not course_id:
            return Response({"error": "course_id"}, status=400)

        course = get_object_or_404(Course, id=course_id)
        subscription_qs = Subscription.objects.filter(user=user, course=course)

        if subscription_qs.exists():
            subscription_qs.delete()
            message = "Подписка удалена"
        else:
            Subscription.objects.create(user=user, course=course)
            message = "Подписка добавлена"

        return Response({"message": message})
