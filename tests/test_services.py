import pytest


@pytest.mark.parametrize("name", ["haveged",
                                  "systemd-timesyncd",
                                  "systemd-resolved",
                                  "systemd-journald",
                                  "mender-client",
                                  "mender-connect",
                                  "NetworkManager",
                                  ])
def test_service(host, name):
    service = host.service(name)
    assert service.is_running
    assert service.is_enabled
