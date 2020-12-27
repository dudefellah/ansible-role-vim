vim
=========

This is a role for installing and configuring a local user vim configuration.
Currently it only supports vim 8+ since it's only making use of the .vim/pack
directory for native package loading and not any third-party package loader.
If you're not using this role to install plugins, you could still use
it to install vim and/or edit your .vimrc on older versions of vim.

Requirements
------------

None.

Role Variables
--------------

Role variables are listed and documented in
[defaults/main.yml](defaults/main.yml). It should be noted here that the
`vim_user` and `vim_group` values must be set when using this role as it
is meant for configuring a local user's configuration and not for global
system configuration.

Dependencies
------------

None.

Example Playbook
----------------

Install a vim, and install vim plugins and a vimrc file for alice:

    - hosts: workstations
      roles:
         - role: dudefellah.vim
           vim_packages:
             - vim
             - vim-airline # install the vim airline plugin package globally
           vim_user: alice
           vim_group: alice
           vim_vimrc_path: .vimrc
           vim_vimrc
           vim_plugin_git_repos:
             - repo: "https://github.com/udalov/kotlin-vim.git"
               dest: "kotlin-vim.vim"

License
-------

GPLv2+

Author Information
------------------

Dan - github.com/dudefellah
