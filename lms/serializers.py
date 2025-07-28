from rest_framework import serializers

from lms.models import Course, Lessons
from users.models import Payments


class LessonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    number_of_lessons = serializers.SerializerMethodField()
    lessons = LessonsSerializer(many=True)

    @staticmethod
    def get_number_of_lessons(instance):
        return instance.lessons.count()

    class Meta:
        model = Course
        fields = "__all__"


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"
