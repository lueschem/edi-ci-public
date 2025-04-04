import time


def test_ntp_sync(host):
    retry = 12
    sleep = 15
    output = ""
    for i in range(retry):
        cmd = host.run("timedatectl")
        assert cmd.rc == 0
        output = cmd.stdout
        if "System clock synchronized: yes" in output:
            return
        elif i + 1 != retry:
            time.sleep(sleep)

    assert "System clock synchronized: yes" in output
