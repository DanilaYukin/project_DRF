from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from lms.models import Course, Lessons
from users.models import User


class LessonTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="admin@lms.ru")
        self.client.force_authenticate(self.user)
        self.course = Course.objects.create(
            title="Test Course",
            description="Test Description",
            owner=self.user
        )

    def test_create_lesson(self):
        """ Тестирование создания урока """
        self.data = {
            "title": "Test",
            "description": "Test",
            "course": self.course.id
        }

        response = self.client.post(
            '/lesson/create/',
            data=self.data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'description': 'Test', 'title': 'Test', 'image': None, 'video_url': None, 'course': 1, 'owner': 1}

        )

        self.assertTrue(
            Lessons.objects.all().exists()
        )

    def test_list_lessons(self):
        """ Тестирование списка уроков """
        lesson = Lessons.objects.create(
            title="Test",
            description="Test",
            course=self.course,
            owner=self.user
        )

        response = self.client.get(
            '/lessons/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        result = response.json()['results'][0]

        self.assertEqual(
            result,
            {
                'id': lesson.id,
                'description': 'Test',
                'title': 'Test',
                'image': None,
                'video_url': None,
                'course': self.course.id,
                'owner': self.user.id
            }
        )

    def test_update_lesson(self):
        """ Тестированрие для обновления урока """
        lesson = Lessons.objects.create(
            title="Test",
            description="Test",
            course=self.course,
            owner=self.user
        )

        self.data = {
            "title": "Test 1",
            "description": "Test 1",
            "course": self.course.id
        }

        response = self.client.put(
            f'/lesson/update/{lesson.id}/',
            data=self.data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {'id': lesson.id, 'description': 'Test 1', 'title': 'Test 1', 'image': None, 'video_url': None,
             'course': self.course.id, 'owner': self.user.id}

        )

    def test_delete_lesson(self):
        """ Тестирование удаления урока """
        lesson = Lessons.objects.create(
            title="Test",
            description="Test",
            course=self.course,
            owner=self.user
        )
        response = self.client.delete(
            f'/lesson/delete/{lesson.id}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Lessons.objects.filter(id=lesson.id).exists()
        )
