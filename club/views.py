from django.db.models import Q
from django.utils import timezone
from django.views.generic import CreateView, FormView, ListView, TemplateView
from django.views.generic.detail import DetailView

from club.forms import MemberForm, MembershipFeePeriodForm
from club.models import Member, MemberRole, MembershipFeePeriod


class ClubView(TemplateView):
    template_name = "club/club.html"


class MemberListView(ListView):
    model = Member


class MemberActiveListView(MemberListView):
    def get_queryset(self):
        today = timezone.now().date()
        return Member.objects.filter(Q(active_until__isnull=True) | Q(active_until__gt=today))


class MemberInactiveListView(MemberListView):
    def get_queryset(self):
        print(self.request.resolver_match.url_name)
        print(self.request.resolver_match.view_name)
        today = timezone.now().date()
        return Member.objects.filter(active_until__lte=today)


class MemberFeeOverdueListView(MemberListView):
    def get_queryset(self):
        last_period = MembershipFeePeriod.objects.last_period()
        if last_period is None:
            return Member.objects.none()
        return Member.objects.exclude(id__in=last_period.members.all())


class MemberBoardListView(MemberListView):
    def get_queryset(self):
        today = timezone.now().date()
        member_ids = MemberRole.objects.filter(
            Q(role=MemberRole.MemberRoleChoice.BOARD) & (Q(active_until__isnull=True) | Q(active_until__gt=today))
        ).values_list("member")
        return Member.objects.filter(id__in=member_ids)


class MemberAuditCommitteeListView(MemberListView):
    def get_queryset(self):
        today = timezone.now().date()
        member_ids = MemberRole.objects.filter(
            Q(role=MemberRole.MemberRoleChoice.AUDIT_COMMITTEE)
            & (Q(active_until__isnull=True) | Q(active_until__gt=today))
        ).values_list("member")
        return Member.objects.filter(id__in=member_ids)


class MemberDetailView(DetailView):
    model = Member

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        print(context["object"].membershipfeeperiod_set.all())

        return context


class MemberCreateView(CreateView):
    model = Member
    form_class = MemberForm


class FeeListView(ListView):
    model = MembershipFeePeriod


class FeeCreateView(FormView):
    template_name = "club/membershipfeeperiod_form.html"
    # model = MembershipFeePeriod
    form_class = MembershipFeePeriodForm
