import pytest


@pytest.mark.parametrize("filename", ["ssh_host_dsa_key.pub",
                                      "ssh_host_ecdsa_key.pub",
                                      "ssh_host_ed25519_key.pub",
                                      "ssh_host_rsa_key.pub"])
def test_ssh_backup_restore(host, filename):
    backup_file = "/data/backup/ssh/{}".format(filename)
    restored_file = "/etc/ssh/{}".format(filename)

    assert host.file(backup_file).exists
    assert host.file(restored_file).exists

    cmd = host.run("diff {} {}".format(backup_file, restored_file))
    assert cmd.stdout == ""
    assert cmd.rc == 0
