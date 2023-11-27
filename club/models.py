from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django_hosts import reverse

from players.models import Player


class Member(models.Model):
    id = models.SlugField(primary_key=True, verbose_name="ID")

    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    player = models.OneToOneField(Player, on_delete=models.SET_NULL, null=True, blank=True)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    nickname = models.CharField(max_length=50, blank=True)

    workspace_email = models.EmailField()
    email_communication_consent = models.BooleanField()
    personal_email = models.EmailField(blank=True)
    address = models.TextField()
    discord_nickname = models.CharField(max_length=30, blank=True, verbose_name="Discord nickname")
    discord_id = models.CharField(max_length=30, blank=True, verbose_name="Discord ID")

    active_since = models.DateField()
    active_until = models.DateField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse("member-detail", kwargs={"pk": self.pk}, host="root")

    def relevant_fees(self):
        return MembershipFeePeriod.objects.filter(active_until__gte=self.active_since)

    def paid_fees(self):
        return self.membershipfeeperiod_set.all()

    def current_fee_paid(self):
        last_period = MembershipFeePeriod.objects.last_period()
        if last_period is None:
            return True
        return self in last_period.members.all()

    def current_role(self):
        today = timezone.now().date()
        last_role = self.memberrole_set.order_by("-active_until").first()
        if last_role is not None and (last_role.active_until is None or last_role.active_until > today):
            return last_role.name()
        else:
            return "Member"

    def __str__(self):
        s = ""

        if self.first_name and self.last_name:
            s = f"{self.first_name} {self.last_name}"

        if self.nickname:
            if s:
                s += f" ({self.nickname})"
            else:
                s = self.nickname

        return s


class MemberRole(models.Model):
    class MemberRoleChoice(models.TextChoices):
        BOARD = ("BOARD", "Board")
        AUDIT_COMMITTEE = ("AUDIT_COMMITTEE", "Audit committee")

    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    role = models.CharField(
        max_length=20,
        choices=MemberRoleChoice.choices,
    )
    active_since = models.DateField()
    active_until = models.DateField(null=True, blank=True)

    def name(self):
        return self.get_role_display()


class MembershipFeePeriodManager(models.Manager):
    def last_period(self):
        return self.order_by("-active_until").first()


class MembershipFeePeriod(models.Model):
    name = models.CharField(max_length=30)
    active_since = models.DateField()
    active_until = models.DateField()
    fee = models.DecimalField(max_digits=15, decimal_places=6)
    members = models.ManyToManyField(Member, blank=True)

    objects = MembershipFeePeriodManager()
