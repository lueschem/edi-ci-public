def test_systemd_overall_status(host):
    cmd = host.run("systemctl is-system-running")
    assert cmd.rc == 0
    assert "running" in cmd.stdout


def test_systemd_analyze_verify(host):
    if host.system_info.codename == "bullseye":
        # systemd-analyze shows false positives on Debian bullseye
        return

    cmd = host.run("systemd-analyze verify --man=no default.target")

    assert cmd.stdout == ""
    assert cmd.stderr == ""
