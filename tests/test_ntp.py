import time


def test_ntp_sync(host):
    retry = 12
    sleep = 15
    for i in range(retry):
        cmd = host.run("timedatectl")
        assert cmd.rc == 0
        if "System clock synchronized: yes" in cmd.stdout:
            return
        elif i + 1 != retry:
            time.sleep(sleep)

    assert "System clock synchronized: yes" in cmd.stdout
