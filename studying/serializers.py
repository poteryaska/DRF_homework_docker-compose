from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from studying.models import Course, Lesson, Subscription
from studying.validators import VideoValidator
from users.serializers import UserSerializer


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [
            VideoValidator(field='video'),
        ]




class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField(read_only=True)
    subscribed = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'
        validators = [
            VideoValidator(field='description'),
        ]

    def get_lessons_count(self, instance):
        return instance.lesson.count()

    def get_subscribed(self, instance):
        request = self.context.get('request')
        if request:
            return Subscription.objects.filter(subscribed=True).exists()
        return False