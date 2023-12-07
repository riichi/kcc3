from django.urls import path

from .views import (
    ClubView,
    FeeCreateView,
    FeeListView,
    MemberActiveListView,
    MemberAuditCommitteeListView,
    MemberBoardListView,
    MemberCreateView,
    MemberDetailView,
    MemberFeeOverdueListView,
    MemberInactiveListView,
    MemberListView,
)

urlpatterns = [
    path("", ClubView.as_view(), name="club"),
    path("members/", MemberListView.as_view(), name="member-list"),
    path("members/active/", MemberActiveListView.as_view(), name="member-active-list"),
    path("members/inactive/", MemberInactiveListView.as_view(), name="member-inactive-list"),
    path("members/fee-overdue/", MemberFeeOverdueListView.as_view(), name="member-fee-overdue-list"),
    path("members/board/", MemberBoardListView.as_view(), name="member-board-list"),
    path("members/audit-committee/", MemberAuditCommitteeListView.as_view(), name="member-audit-committee-list"),
    path("members/create/", MemberCreateView.as_view(), name="member-create"),
    path("members/get/<slug:pk>/", MemberDetailView.as_view(), name="member-detail"),
    # path("members/<slug:pk>/edit/", MemberDetailView.as_view(), name="member-edit"),
    path("fees/", FeeListView.as_view(), name="fee-list"),
    path("fees/create/", FeeCreateView.as_view(), name="fee-create"),
]
