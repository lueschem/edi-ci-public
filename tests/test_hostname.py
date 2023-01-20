import re


def test_hostname(host):
    assert host.system_info.distribution == "debian"

    cmd = host.run("hostnamectl --transient")
    assert cmd.rc == 0
    transient_hostname = cmd.stdout
    cmd = host.run("hostnamectl --static")
    static_hostname = cmd.stdout

    assert static_hostname == transient_hostname

    if host.system_info.codename == "bullseye":
        return

    hostname_suffix = static_hostname.split("-")[-1]

    suffix_regexp = r'^[0-9a-fA-F]{12}$'

    assert re.match(suffix_regexp, hostname_suffix) is not None
