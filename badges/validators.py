from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class ImageMinResolutionValidator:
    def __init__(self, width: int, height: int | None = None):
        self.width = width
        self.height = width if height is None else height

    def __call__(self, value):
        if value.width < self.height or value.height < self.height:
            raise ValidationError(f"The image resolution must be at least " f"{self.width}x{self.height}.")

    def __eq__(self, o: object) -> bool:
        return isinstance(o, ImageMinResolutionValidator) and self.width == o.width and self.height == o.height


@deconstructible
class ImageMaxResolutionValidator:
    def __init__(self, width: int, height: int | None = None):
        self.width = width
        self.height = width if height is None else height

    def __call__(self, value):
        if value.width > self.height or value.height > self.height:
            raise ValidationError(f"The image resolution must be at most " f"{self.width}x{self.height}.")

    def __eq__(self, o: object) -> bool:
        return isinstance(o, ImageMaxResolutionValidator) and self.width == o.width and self.height == o.height


def image_square_validator(value):
    if value.width != value.height:
        raise ValidationError("The image dimensions must be a square.")


@deconstructible
class MaxFileSizeValidator:
    def __init__(self, size):
        self.size = size

    @staticmethod
    def human_readable_size(size):
        # ruff: noqa: B007
        for unit in ["B", "kB", "MB", "GB", "TB"]:
            if size < 1000.0:
                break
            size /= 1000.0

        return f"{size:.1f}{unit}"

    def __call__(self, value):
        if value.size > self.size:
            size_str = self.human_readable_size(self.size)
            raise ValidationError(f"The file size cannot exceed {size_str}.")

        return value

    def __eq__(self, o: object) -> bool:
        return isinstance(o, MaxFileSizeValidator) and self.size == o.size
