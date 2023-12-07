from django import template
from django_hosts import reverse

from club.models import Member

register = template.Library()


class Breadcrumb:
    def __init__(self, parent_url_name: str | None, url_name: str, link_text: str | None = None):
        self.parent_url_name = parent_url_name
        self.view_name = url_name
        self.link_text = link_text

    def get_link_text(self, request):
        return self.link_text

    def get_url(self, request):
        return reverse(self.view_name, kwargs=self.get_url_kwargs(request), host="root")

    def get_url_kwargs(self, request):
        return {}


class MemberBreadcrumb(Breadcrumb):
    def get_link_text(self, request):
        return str(Member.objects.get(pk=self.get_pk(request)))

    def get_url_kwargs(self, request):
        return {"pk": self.get_pk(request)}

    @staticmethod
    def get_pk(request):
        return request.resolver_match.kwargs["pk"]


BREADCRUMBS: dict[str, Breadcrumb] = {}


def add_breadcrumb(breadcrumb: Breadcrumb):
    BREADCRUMBS[breadcrumb.view_name] = breadcrumb


def add_breadcrumb_copy(url_name: str, alternate_url_name: str):
    BREADCRUMBS[alternate_url_name] = BREADCRUMBS[url_name]


add_breadcrumb(Breadcrumb(None, "club", "Club"))
add_breadcrumb(Breadcrumb("club", "member-list", "Members"))
add_breadcrumb_copy("member-list", "member-active-list")
add_breadcrumb_copy("member-list", "member-inactive-list")
add_breadcrumb_copy("member-list", "member-fee-overdue-list")
add_breadcrumb_copy("member-list", "member-board-list")
add_breadcrumb_copy("member-list", "member-audit-committee-list")
add_breadcrumb(MemberBreadcrumb("member-list", "member-detail"))
add_breadcrumb(Breadcrumb("member-list", "member-create", "Create"))
add_breadcrumb(Breadcrumb("club", "fee-list", "Fees"))
add_breadcrumb(Breadcrumb("fee-list", "fee-create", "Create"))


@register.inclusion_tag("common/breadcrumbs.html", takes_context=True)
def breadcrumbs(context):
    request = context["request"]
    result = []
    url_name = request.resolver_match.url_name
    if url_name not in BREADCRUMBS:
        raise Exception(f"URL name {url_name} unknown, cannot create breadcrumbs")
    current_breadcrumb = BREADCRUMBS[url_name]

    while current_breadcrumb is not None:
        result.insert(
            0,
            {
                "url": current_breadcrumb.get_url(request),
                "link_text": current_breadcrumb.get_link_text(request),
            },
        )

        current_breadcrumb = BREADCRUMBS.get(current_breadcrumb.parent_url_name)

    return {
        "breadcrumbs": result,
    }
