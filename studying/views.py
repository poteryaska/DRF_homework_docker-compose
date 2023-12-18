from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from studying.models import Course, Lesson, Subscription
from studying.permissions import IsModerator, IsCourseOwner, IsLessonOwner
from studying.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated]
        elif self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated, IsCourseOwner | IsModerator]
        elif self.action == 'update':
            permission_classes = [IsAuthenticated, IsModerator | IsCourseOwner]
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsCourseOwner]
        return [permission() for permission in permission_classes]

class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    lookup_field = 'id'
    def perform_create(self, serializer):
        new_subscription = serializer.save(user=self.request.user)
        new_subscription.save()

class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    queryset = Subscription.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsLessonOwner]

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModerator | IsLessonOwner]


class LessonUpdateAPIView(generics.UpdateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsModerator | IsLessonOwner]

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsLessonOwner]
