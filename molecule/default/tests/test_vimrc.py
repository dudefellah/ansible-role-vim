
import json

import os

import re

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_config_files(host):
    user_home = "/home/alice"
    assert host.file("{home}/.vimrc".format(home=user_home)).user == "alice"
    assert host.file("{home}/.vimrc".format(home=user_home)).group == "alice"
    assert host.file("{home}/.vimrc".format(home=user_home)).mode == 0o644
    assert host.file("{home}/.vimrc".format(home=user_home)).exists

    assert host.file(
        "{home}/.vim/pack/ansible-role-vim/start/kotlin-vim.vim".format(home=user_home)
    ).exists

    assert host.file(
        "{home}/.vim/pack/ansible-role-vim/start/ctrlp.vim".format(home=user_home)
    ).exists
    assert host.file(
        "{home}/.vim/pack/ansible-role-vim/start/ctrlp.vim/.checksum".format(home=user_home)
    ).exists
