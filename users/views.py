from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.models import User, Payments
from users.serializers import PaymentsSerializer
from users.serializers import UserSerializer
from users.services import (
    create_product_course,
    create_price_product,
    create_product_lesson,
    create_session,
)


class PaymentsListAPIView(generics.ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ("course", "lessons")
    ordering_fields = ("date", "payment_method")


class UserCreateApiView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permissions_class = AllowAny

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()

    def perform_create(self, serializer):
        payment = serializer.save(user=self.request.user)
        if payment.course:
            course_product = create_product_course(payment.course.title)
            price_course = create_price_product(payment.payment_amount, course_product)
            session_id_course, link_course = create_session(price_course)
            payment.session_id_course = session_id_course
            payment.link_course = link_course

        if payment.lessons:
            lesson_product = create_product_lesson(payment.lessons.title)
            price_lesson = create_price_product(payment.payment_amount, lesson_product)
            session_id_lesson, link_lesson = create_session(price_lesson)
            payment.session_id_lesson = session_id_lesson
            payment.link_lesson = link_lesson

        payment.save()
