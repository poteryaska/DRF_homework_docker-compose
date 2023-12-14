from  rest_framework.permissions import BasePermission

from users.models import UserRoles
from  studying.models import Course, Lesson

class IsModerator(BasePermission):
    massage = "Вы не являетесь модератором"

    def has_permission(self, request, view):
        if request.user.role == UserRoles.MODERATOR:
            return True
        return False

class IsLessonOwner(BasePermission):
    massage = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.lesson_owner:
            return True
        return False

class IsCourseOwner(BasePermission):
    massage = "Вы не являетесь владельцем"

    def has_object_permission(self, request, view, obj):
        if request.user == obj.course_owner:
            return True
        return False
