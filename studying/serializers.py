from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from studying.models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons_count(self, instance):
        return instance.lesson.count()


# class CourseListSerializer(serializers.ModelSerializer):
#     # lessons = SlugRelatedField(slug_field="name", queryset=Lesson.objects.all())
#     class Meta:
#         model = Course
#         fields = ('name',)
#
# class CourseDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Course
#         fields = '__all__'
#


