# pip install userhome salt

```
pip install --user salt-ssh
 1000  ls -lahrt
 1001  export PATH=$PATH:~/.local/bin
 1002  salt-ssh
```
# salt-api
```
salt-api
curl http://localhost:8000/run -H 'Accept: application/x-yaml' -d
client='ssh' -d tgt='*' -d fun='test.ping' -d
roster_file='/etc/salt/roster_pengyao
```

# sudo fix -n
```
oi# bigg01 sudo
__opts__ = {
            'sudocmdlist': ""
           }

def six_sudo_wrapper(cmd):
    if __opts__['sudocmdlist']:
        six_get_sudocmdlist = __opts__['sudocmdlist']
        sudocmd = which('sudo')
        sudo_check = False
        for check_cmd in six_get_sudocmdlist:
            if isinstance(cmd, str):
                if cmd.find(check_cmd) != -1:
                    sudo_check = True
                    log.info("six_sudo_wrapper: found '{0}' in list using sudo".format(cmd))
            if isinstance(cmd, list):
                if check_cmd in cmd:
                    log.info("six_sudo_wrapper: found '{0}' in list using sudo".format(cmd[0]))
                    sudo_check = True
            log.info(cmd)
        if sudo_check:
            if isinstance(cmd, str):
                cmd = sudocmd + '-n' + ' ' + cmd
            if isinstance(cmd, list):
                cmd.insert(0, sudocmd)
                cmd.insert(1, '-n')
        return cmd
    else:
        return cmd
# bigg01 sudo end
```

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
