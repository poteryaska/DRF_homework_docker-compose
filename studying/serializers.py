from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from studying.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


class LessonListSerializer(serializers.ModelSerializer):
    lesson = SlugRelatedField(slug_field="name", queryset=Course.objects.all())
    class Meta:
        model = Lesson
        fields = ('name',)

class LessonDetailSerializer(serializers.ModelSerializer):
    lesson = CourseSerializer()
    class Meta:
        model = Lesson
        fields = ('name', 'lesson')