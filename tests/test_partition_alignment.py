import pytest


@pytest.mark.parametrize("partition_number, is_error", [(1, True), (2, True), (3, True), (4, False)])
def test_partition_alignment(host, partition_number, is_error):
    with host.sudo():
        cmd = host.run("mount | grep 'on / '")
        assert cmd.rc == 0

    root_device = cmd.stdout.split()[0].rstrip("1234567890").rstrip("p")

    with host.sudo():
        cmd = host.run(f"parted {root_device} align-check optimal {partition_number}")
        assert cmd.rc == 0

    assert f"{partition_number} aligned" in cmd.stdout
