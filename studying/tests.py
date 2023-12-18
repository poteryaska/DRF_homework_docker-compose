from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import AccessToken

from studying.models import Course, Lesson, Subscription
from users.models import User


class BaseTestCase(APITestCase):
    email = 'test@mail.com'
    password = '12345678'

    def setUp(self):
        self.user = User.objects.create(
            email=self.email,
            first_name='Admin',
            last_name='Admin',
            phone='12345678',
            role='member',
            is_staff=True,
            is_superuser=True,
            is_active=True,
        )
        self.user.set_password(self.password)
        self.user.save()

        self.course = Course.objects.create(
            name='Test Course',
            description='Test Description',
            course_owner=self.user,
        )

        self.lesson = Lesson.objects.create(
            name='Test Lesson',
            description='Test Description',
            course=self.course,
            lesson_owner=self.user,
        )

        self.subscription = Subscription.objects.create(
            course=self.course,
            user=self.user,
            subscribed=True,
        )

        self.client = APIClient()
        # Get Access Token For Current User (Moderator)
        access_token = AccessToken.for_user(self.user)
        self.client.force_authenticate(user=self.user, token=access_token)

    def tearDown(self):
        self.course.delete()
        self.user.delete()
        self.subscription.delete()

class LessonTestCases(BaseTestCase):
    def test_lesson_create(self):
        response = self.client.post(reverse("studying:lesson-create"), data={
            'name': 'Test Lesson',
            'description': 'Test Description',
            'lesson_owner': self.user.id,
            'course': self.course.id,
        }
                                    )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(),
                         {
                             'id': 3,
                             'name': 'Test Lesson',
                             'description': 'Test Description',
                             'preview': None,
                             'video': None,
                             'course': self.course.pk,
                             'lesson_owner': self.user.pk,
                         }
                         )

    def test_lesson_get_list(self):
        response = self.client.get(reverse("studying:lesson-list"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {
            'count': 1,
            'next': None,
            'previous': None,
            'results': [
                {'id': self.lesson.pk,
                 'course': self.course.pk,
                 'name': 'Test Lesson',
                 'description': 'Test Description',
                 'preview': None,
                 'video': None,
                 'lesson_owner': self.user.pk,

                 }
            ]
        }
                         )

    def test_get_lesson(self):
        response = self.client.get(reverse("studying:lesson-get", args=[self.lesson.pk]))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {
                             'id': self.lesson.pk,
                             'name': 'Test Lesson',
                             'description': 'Test Description',
                             'preview': None,
                             'video': None,
                             'course': self.course.pk,
                             'lesson_owner': self.user.pk,
                         }
                         )

    def test_lesson_update(self):
        response = self.client.patch(reverse("studying:lesson-update", args=[self.lesson.pk]), data={
            'name': 'Test Lesson Update',
            'description': 'Test Description Update',
        })

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(),
                         {
                             'id': self.lesson.pk,
                             'name': 'Test Lesson Update',
                             'description': 'Test Description Update',
                             'preview': None,
                             'video': None,
                             'course': self.course.pk,
                             'lesson_owner': self.user.pk,
                         }
                         )

    def test_lesson_delete(self):
        response = self.client.delete(reverse("studying:lesson-delete", args=[self.lesson.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubscriptionTestCases(BaseTestCase):
    def test_subscription_create(self):
        response = self.client.post(reverse("studying:subscription-create"), data={
            'course': self.course.pk,
            'user': self.user.pk,
            'subscribed': False,
        }
                                    )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json(),
                         {
                             'id': 7,
                             'course': self.course.pk,
                             'user': self.user.pk,
                             'subscribed': False,
                         }
                         )


    def test_unsubscribed(self):
        response = self.client.delete(reverse("studying:subscription-delete", args=[self.subscription.pk]))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)