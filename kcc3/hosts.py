from django_hosts import host, patterns

host_patterns = patterns(
    "",
    host(r"fanpai", "kcc3.urls", name="root"),
    host(r"yakuman", "yakumans.urls", name="yakumans"),
)
