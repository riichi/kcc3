from django.core.exceptions import ValidationError


class ImageMinResolutionValidator:
    def __init__(self, width: int, height: int = None):
        self.width = width
        self.height = width if height is None else height

    def __call__(self, value):
        if value.width < self.height or value.height < self.height:
            raise ValidationError(
                f'The image resolution must be at least '
                f'{self.width}x{self.height}.')


class ImageMaxResolutionValidator:
    def __init__(self, width: int, height: int = None):
        self.width = width
        self.height = width if height is None else height

    def __call__(self, value):
        if value.width > self.height or value.height > self.height:
            raise ValidationError(
                f'The image resolution must be at most '
                f'{self.width}x{self.height}.')


class ImageSquareValidator:
    def __call__(self, value):
        if value.width != value.height:
            raise ValidationError('The image dimensions must be a square.')


class MaxFileSizeValidator:
    def __init__(self, size):
        self.size = size

    @staticmethod
    def human_readable_size(size):
        for unit in ['B', 'kB', 'MB', 'GB', 'TB']:
            if size < 1000.:
                break
            size /= 1000.

        return f"{size:.1f}{unit}"

    def __call__(self, value):
        if value.size > self.size:
            size_str = self.human_readable_size(self.size)
            raise ValidationError(f'The file size cannot exceed {size_str}.')

        return value
