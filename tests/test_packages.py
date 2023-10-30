import pytest


@pytest.mark.parametrize("name", ["edi-boot-shim",
                                  "systemd-timesyncd",
                                  "fdisk",
                                  "parted",])
def test_packages(host, name):
    pkg = host.package(name)
    assert pkg.is_installed
