from django_hosts import patterns, host

host_patterns = patterns(
    '',
    host(r'', 'kcc3.urls', name='root'),
    host(r'yakuman', 'yakumans.urls', name='yakumans'),
)
