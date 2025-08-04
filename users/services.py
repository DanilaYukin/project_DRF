import stripe
from config.settings import STRIPE_SECRET_KEY


def create_product_course(course):
    stripe.api_key = STRIPE_SECRET_KEY
    product = stripe.Product.create(name=course)
    return product


def create_product_lesson(lesson):
    stripe.api_key = STRIPE_SECRET_KEY
    product = stripe.Product.create(name=lesson)
    return product


def create_price_product(payment_amount, product):

    price = stripe.Price.create(
        currency="rub",
        unit_amount=int(payment_amount * 100),
        product=product.id,
    )
    return price


def create_session(price):

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price.id, "quantity": 1}],
        mode="payment",
    )
    return session.id, session.url
