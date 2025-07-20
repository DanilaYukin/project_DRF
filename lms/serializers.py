from rest_framework import serializers

from lms.models import Course, Lessons


class CourseSerializer(serializers.ModelSerializer):
    model = Course
    fields = ['title', 'description']


class LessonsSerializer(serializers.ModelSerializer):
    model = Lessons
    fields = ['title', 'description', 'course']
