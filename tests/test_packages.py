import pytest


@pytest.mark.parametrize("name", ["edi-boot-shim", "systemd-timesyncd", ])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed
