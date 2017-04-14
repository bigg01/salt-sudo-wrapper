```
 

 salt-ssh  atomic1 grains.get test
Permission denied for host atomic1, do you want to deploy the salt-ssh key? (password required):
[Y/n] y
Password for guo@atomic1:
atomic1:
    True
$ salt-ssh  atomic1 grains.get test
atomic1:
    True
$ salt-ssh  atomic1 test.ping
atomic1:
    True


$ salt-ssh  atomic1 state.apply test
atomic1:
----------
          ID: bison
    Function: pkg.installed
      Result: False
     Comment: Error occurred installing package(s). Additional info follows:

              errors:
                  - Failed to start transient scope unit: Interactive authentication required.
     Started: 21:03:16.196830
    Duration: 35604.121 ms
     Changes:

Summary for atomic1
------------
Succeeded: 0
Failed:    1
------------


Total states run:     1
Total run time:  35.604 s

 
$ salt-ssh  atomic1 config.get sudocmdlist
atomic1:
    - service
    - systemctl
    - yum
    - zypper
    - dnf
    - systemd-run
$ cat Saltfile
salt-ssh:
  config_dir: /home/guo/salt-ssh/
  ssh_max_procs: 30
  ssh_wipe: True
  ssh_log_file: /home/guo/salt-ssh/salt-ssh-log.log
  #ssh_minion_opts:

$ tree salt-ssh/
salt-ssh/
├── master
├── roster
├── salt
│   ├── config
│   │   └── pki
│   │       └── ssh
│   │           ├── salt-ssh.rsa
│   │           └── salt-ssh.rsa.pub
│   ├── salt-ssh-log.log
└── salt-ssh-log.log

37 directories, 27 files
$ cat salt-ssh/master
root_dir: /home/guo/salt-ssh/salt
pki_dir: config/pki
ssh_log_file: salt-ssh/
ssh_use_home_key: True


fileserver_backend:
  - roots

file_roots:
  base:
    - /home/guo/states


pillar_roots:
  base:
    - /home/guo/states/pillar



$ cat salt-ssh/roster
# Sample salt-ssh config file
#web1:
#  host: 192.168.42.1 # The IP addr or DNS hostname
#  user: fred         # Remote executions will be executed as user fred
#  passwd: foobarbaz  # The password to use for login, if omitted, keys are used
#  sudo: True         # Whether to sudo to root, not enabled by default
#web2:
#  host: 192.168.42.2

atomic1:
  host: 10.0.0.3
  user: guo         # Remote executions will be executed as user fred
  #sudo: True         # Whether to sudo to root, not enabled by default
  grains:
    test: True
  minion_opts:
    sudocmdlist:
      - service
      - systemctl
      - yum
      - zypper
      - dnf
      - systemd-run
```
