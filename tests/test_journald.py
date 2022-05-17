def test_journald_no_persistent_logging(host):
    assert not host.file("/var/log/journal").exists

