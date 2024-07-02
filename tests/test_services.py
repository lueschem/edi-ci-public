import pytest


@pytest.mark.parametrize("name", ["haveged",
                                  "systemd-timesyncd",
                                  "systemd-journald",
                                  "mender-connect",
                                  "NetworkManager",
                                  ])
def test_service(host, name):
    service = host.service(name)
    assert service.is_running
    assert service.is_enabled


def test_mender_update_services(host):
    mender_client_pkg = host.package("mender-client")

    if mender_client_pkg.is_installed:
        mender_client = host.service("mender-client")
        assert mender_client.is_running
        assert mender_client.is_enabled
    else:
        mender_updated = host.service("mender-updated")
        mender_authd = host.service("mender-authd")
        assert mender_updated.is_running and mender_authd.is_running
        assert mender_updated.is_enabled and mender_authd.is_enabled
