import datetime
import itertools

from django import forms
from django.forms import Form, ModelForm

from club.models import Member, MembershipFeePeriod


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = (
            "first_name",
            "last_name",
            "nickname",
            "workspace_email",
            "personal_email",
            "email_communication_consent",
            "address",
            "discord_nickname",
            "discord_id",
            "active_since",
            "active_until",
        )


def get_fee_choices() -> list[tuple[str, str]]:
    fees = [create_half_year_fee_period(year, half) for year, half in itertools.product(range(2020, 2030), (1, 2))]
    return [(str(idx), fee.name) for idx, fee in enumerate(fees)]


def create_half_year_fee_period(year: int, half: int) -> MembershipFeePeriod:
    name = f"{year}H{half}"
    if half == 1:
        active_since = datetime.date(year, 1, 1)
        active_until = datetime.date(year, 7, 1)
    elif half == 2:
        active_since = datetime.date(year, 7, 1)
        active_until = datetime.date(year + 1, 1, 1)
    else:
        raise Exception(f"Half {half} not valid")

    return MembershipFeePeriod(name=name, active_since=active_since, active_until=active_until)


class MembershipFeePeriodForm(Form):
    period = forms.ChoiceField(choices=get_fee_choices())
    fee = forms.DecimalField(max_digits=10, decimal_places=2)
