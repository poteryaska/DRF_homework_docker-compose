from django.urls import path

from studying.apps import StudyingConfig
from rest_framework.routers import DefaultRouter

from studying.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonDestroyAPIView, LessonUpdateAPIView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView

app_name = StudyingConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lesson/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-get'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lesson/delete/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
    path('course/<int:pk>/create_sub/', SubscriptionCreateAPIView.as_view(), name='subscription-create'),
    path('course/<int:pk>/delete_sub/', SubscriptionDestroyAPIView.as_view(), name='subscription-delete'),

] + router.urls