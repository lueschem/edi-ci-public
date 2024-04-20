import pytest


@pytest.mark.parametrize("path, user, group, mode",  [
    ("/etc/hosts", "root", "root", 0o644),
    ("/etc/gshadow", "root", "shadow", 0o640),
    ("/etc/hostname", "root", "root", 0o644),
    ("/usr/bin", "root", "root", 0o755),
    ("/dev/null", "root", "root", 0o666),
])
def test_permissions(host, path, user, group, mode):
    test_file = host.file(path)
    assert test_file.user == user
    assert test_file.group == group
    assert test_file.mode == mode
