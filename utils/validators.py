from django.core.exceptions import ValidationError


def validate_post_title(value):
    if not value or len(value) < 5:
        raise ValidationError("제목은 최소 5자 이상이어야 합니다.")
    elif len(value) > 50:
        raise ValidationError("제목은 최대 50자를 초과할 수 없습니다.")


def validate_post_content(value):
    if not value or len(value) < 10:
        raise ValidationError("설명은 10글자 이상이어야 합니다.")
