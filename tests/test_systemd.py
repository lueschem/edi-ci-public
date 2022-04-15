import pytest


def test_systemd_overall_status(host):
    cmd = host.run("systemctl is-system-running")
    assert cmd.rc == 0
    assert "running" in cmd.stdout
