from rest_framework import serializers

from lms.models import Course, Lessons


class CourseSerializer(serializers.ModelSerializer):
    model = Course
    fields = '__all__'


class LessonsSerializer(serializers.ModelSerializer):
    model = Lessons
    fields = '__all__'
