from rest_framework import serializers

from lms.models import Course, Lessons, Subscription
from lms.validators import DescriptionUrlValidator


class LessonsSerializer(serializers.ModelSerializer):
    description = serializers.CharField(validators=[DescriptionUrlValidator(field='description')])

    class Meta:
        model = Lessons
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    number_of_lessons = serializers.SerializerMethodField()
    lessons = LessonsSerializer(many=True, read_only=True)

    @staticmethod
    def get_number_of_lessons(instance):
        return instance.lessons.count()

    class Meta:
        model = Course
        fields = "__all__"
        validators = [DescriptionUrlValidator(field='description')]


class SubscriptionSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    def get_is_subscribed(self, course):
        user = self.context['request'].user
        return Subscription.objects.filter(user=user, course=course).exists()

    class Meta:
        model = Subscription
        fields = '__all__'
