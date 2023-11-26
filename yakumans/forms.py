from django.forms import SelectMultiple, TypedMultipleChoiceField

from yakumans import yakumans
from yakumans.yakumans import yakuman_by_name


class YakumansSelectMultiple(SelectMultiple):
    def format_value(self, value):
        if value is None:
            return []

        return [x.name for x in value]

    def value_from_datadict(self, data, files, name):
        value = super().value_from_datadict(data, files, name)

        print(value)
        return [yakumans.yakuman_by_name(yaku_id) for yaku_id in value]


class YakumansChoiceField(TypedMultipleChoiceField):
    widget = YakumansSelectMultiple

    def __init__(self, **kwargs):
        kwargs["empty_value"] = []
        kwargs["choices"] = ((yaku, yaku.verbose_name) for yaku in yakumans.YAKUMANS_BY_NAME)
        kwargs["coerce"] = yakuman_by_name

        super().__init__(**kwargs)
