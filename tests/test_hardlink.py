def test_hardlink(host):
    cmd = host.run("find /usr/bin/ -samefile /usr/bin/perl")
    assert cmd.stdout.count('/usr/bin/perl') > 1
