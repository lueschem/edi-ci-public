import pytest


def test_ntp_sync(host):
    cmd = host.run("timedatectl")
    assert cmd.rc == 0
    assert "System clock synchronized: yes" in cmd.stdout