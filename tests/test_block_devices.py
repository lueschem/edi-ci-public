import re


def test_root_device(host):
    cmd = host.run("df / --output=pcent")
    assert cmd.rc == 0
    match = re.search(r"(\d{1,3})%", cmd.stdout)
    assert match
    # if the usage is below 50% then the root device got properly resized
    assert int(match.group(1)) < 50


def test_resize_completion(host):
    assert host.file("/etc/edi-resize-rootfs.done").exists
