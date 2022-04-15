def test_upgrade_available(host):
    with host.sudo():
        cmd = host.run("fw_printenv upgrade_available")
        assert cmd.rc == 0
        assert "upgrade_available=0" in cmd.stdout
