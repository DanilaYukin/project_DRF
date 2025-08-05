import re
from rest_framework import validators, serializers


class DescriptionUrlValidator:
    """Проверка что в описании нет ссылки на другие материалы, кроме youtube.com"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        value = value.get(self.field)

        if value is None:
            return value

        if not isinstance(value, str):
            raise serializers.ValidationError(
                {self.field: "Поле должно быть строкой"},
                code="invalid_type"
            )

        urls = re.findall(r"https?://[^\s]+", value)
        for url in urls:
            if "youtube.com" not in url:
                raise validators.ValidationError(
                    f"Сторонние ссылки запрещены. Разрешены только ссылки на YouTube. Найдена запрещённая ссылка: {url}"
                )
