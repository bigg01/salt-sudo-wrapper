# six wrapper module
bigg01 detect if sudo needed or not
six_sudo_wrapper: found command in list using sudo
```sh
cat /etc/salt/minion.d/sudo.conf
sudocmdlist:
 - service
 - systemctl
 - yum
 - zypper
 - dnf
 - systemd-run
```
```sh
salt-call --local state.single pkg.removed name=bison  sudo=True -l info
[INFO    ] Loading fresh modules for state activity
[ERROR   ] Exception raised when processing __virtual__ function for npm. Module will not be loaded global name '__opts__' is not defined
[WARNING ] salt.loaded.int.module.npm.__virtual__() is wrongly returning `None`. It should either return `True`, `False` or a new name. If you're the developer of the module 'npm', please fix this.
[INFO    ] Running state [bison] at time 17:11:27.731004
[INFO    ] Executing state pkg.removed for bison
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] Executing command ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n'] in directory '/root'
[INFO    ] ['dnf', '-y', 'remove', 'bison']
[INFO    ] ['dnf', '-y', 'remove', 'bison']
[INFO    ] ['dnf', '-y', 'remove', 'bison']
[INFO    ] ['dnf', '-y', 'remove', 'bison']
[INFO    ] ['dnf', '-y', 'remove', 'bison']
[INFO    ] ['dnf', '-y', 'remove', 'bison']
[INFO    ] six_sudo_wrapper: found command in list using sudo
[INFO    ] Executing command ['/bin/sudo', 'dnf', '-y', 'remove', 'bison'] in directory '/root'
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] Executing command ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n'] in directory '/root'
[INFO    ] Made the following changes:
'bison' changed from '3.0.4-4.fc24' to 'absent'

[INFO    ] Loading fresh modules for state activity
[INFO    ] Completed state [bison] at time 17:11:38.679058 duration_in_ms=10948.054
local:
----------
          ID: bison
    Function: pkg.removed
      Result: True
     Comment: All targeted packages were removed.
     Started: 17:11:27.731004
    Duration: 10948.054 ms
     Changes:
              ----------
              bison:
                  ----------
                  new:
                  old:
                      3.0.4-4.fc24

Summary for local
------------
Succeeded: 1 (changed=1)
Failed:    0
------------
Total states run:     1
Total run time:  10.948 s
 root  usr  lib  …  site-packages  salt  modules  #  salt-call --local state.single pkg.installed name=bison  sudo=True -l info
[INFO    ] Loading fresh modules for state activity
[ERROR   ] Exception raised when processing __virtual__ function for npm. Module will not be loaded global name '__opts__' is not defined
[WARNING ] salt.loaded.int.module.npm.__virtual__() is wrongly returning `None`. It should either return `True`, `False` or a new name. If you're the developer of the module 'npm', please fix this.
[INFO    ] Running state [bison] at time 17:11:45.433167
[INFO    ] Executing state pkg.installed for bison
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] Executing command ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n'] in directory '/root'
[INFO    ] ['dnf', '--quiet', 'clean', 'expire-cache']
[INFO    ] ['dnf', '--quiet', 'clean', 'expire-cache']
[INFO    ] ['dnf', '--quiet', 'clean', 'expire-cache']
[INFO    ] ['dnf', '--quiet', 'clean', 'expire-cache']
[INFO    ] ['dnf', '--quiet', 'clean', 'expire-cache']
[INFO    ] ['dnf', '--quiet', 'clean', 'expire-cache']
[INFO    ] six_sudo_wrapper: found command in list using sudo
[INFO    ] Executing command ['/bin/sudo', 'dnf', '--quiet', 'clean', 'expire-cache'] in directory '/root'
[INFO    ] Executing command ['dnf', '--quiet', 'check-update'] in directory '/root'
[INFO    ] ['systemd-run', '--scope', 'dnf', '-y', '--best', '--allowerasing', 'install', 'bison']
[INFO    ] ['systemd-run', '--scope', 'dnf', '-y', '--best', '--allowerasing', 'install', 'bison']
[INFO    ] ['systemd-run', '--scope', 'dnf', '-y', '--best', '--allowerasing', 'install', 'bison']
[INFO    ] ['systemd-run', '--scope', 'dnf', '-y', '--best', '--allowerasing', 'install', 'bison']
[INFO    ] ['systemd-run', '--scope', 'dnf', '-y', '--best', '--allowerasing', 'install', 'bison']
# six wrapper module
[INFO    ] ['systemd-run', '--scope', 'dnf', '-y', '--best', '--allowerasing', 'install', 'bison']
[INFO    ] six_sudo_wrapper: found command in list using sudo
[INFO    ] Executing command ['/bin/sudo', 'systemd-run', '--scope', 'dnf', '-y', '--best', '--allowerasing', 'install', 'bison'] in directory '/root'
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] Executing command ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n'] in directory '/root'
[INFO    ] Made the following changes:
'bison' changed from 'absent' to '3.0.4-4.fc24'

[INFO    ] Loading fresh modules for state activity
[INFO    ] Completed state [bison] at time 17:12:11.203692 duration_in_ms=25770.525
local:
----------
          ID: bison
    Function: pkg.installed
      Result: True
     Comment: The following packages were installed/updated: bison
     Started: 17:11:45.433167
    Duration: 25770.525 ms
     Changes:
              ----------
              bison:
                  ----------
                  new:
                      3.0.4-4.fc24
                  old:

Summary for local
------------
Succeeded: 1 (changed=1)
Failed:    0
------------
Total states run:     1
Total run time:  25.771 s
```


```sh
sudo salt-call --local state.sls bison -l debug
....
[INFO    ] Executing state pkg.installed for bison
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
....
[INFO    ] Executing command ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n'] in directory '/root'
....
[INFO    ] ['dnf', '--quiet', 'clean', 'expire-cache']
[INFO    ] six_sudo_wrapper: found command in list using sudo # --> tkggo wrapper
[INFO    ] Executing command ['/bin/sudo', 'dnf', '--quiet', 'clean', 'expire-cache'] in directory '/root' # --> tkggo wrapper
[DEBUG   ] output:
[INFO    ] Executing command ['dnf', '--quiet', 'check-update'] in directory '/root'
[DEBUG   ] Failed to get holds, versionlock plugin is probably not installed
[INFO    ] ['systemd-run', '--scope', 'dnf', '-y', '--best', '--allowerasing', 'install', 'bison']
[INFO    ] ['systemd-run', '--scope', 'dnf', '-y', '--best', '--allowerasing', 'install', 'bison']
[INFO    ] ['systemd-run', '--scope', 'dnf', '-y', '--best', '--allowerasing', 'install', 'bison']
[INFO    ] ['systemd-run', '--scope', 'dnf', '-y', '--best', '--allowerasing', 'install', 'bison']
[INFO    ] ['systemd-run', '--scope', 'dnf', '-y', '--best', '--allowerasing', 'install', 'bison']
[INFO    ] ['systemd-run', '--scope', 'dnf', '-y', '--best', '--allowerasing', 'install', 'bison']
[INFO    ] six_sudo_wrapper: found command in list using sudo # --> tkggo wrapper
[INFO    ] Executing command ['/bin/sudo', 'systemd-run', '--scope', 'dnf', '-y', '--best', '--allowerasing', 'install', 'bison'] in directory '/root' # --> tkggo wrapper
.....
[INFO    ] six_sudo_wrapper: found command in list using sudo # --> tkggo wrapper
[INFO    ] Executing command ['/bin/sudo', 'dnf', '-y', 'remove', 'bison'] in directory '/root' # --> tkggo wrapper
[INFO    ] ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n']
[INFO    ] Executing command ['rpm', '-qa', '--queryformat', '%{NAME}_|-%{EPOCH}_|-%{VERSION}_|-%{RELEASE}_|-%{ARCH}_|-(none)\n'] in directory '/root'
[INFO    ] Made the following changes:
'bison' changed from '3.0.4-4.fc24' to 'absent'

local:
----------
          ID: install bison rpm
    Function: pkg.installed
        Name: bison
      Result: True
     Comment: The following packages were installed/updated: bison
     Started: 20:47:33.283307
    Duration: 27584.772 ms
     Changes:
              ----------
              bison:
                  ----------
                  new:
                      3.0.4-4.fc24
                  old:
----------
          ID: remove bison rpm
    Function: pkg.removed
        Name: bison
      Result: True
     Comment: All targeted packages were removed.
     Started: 20:48:00.878157
    Duration: 7460.95 ms
     Changes:
              ----------
              bison:
                  ----------
                  new:
                  old:
                      3.0.4-4.fc24

Summary for local
------------
Succeeded: 2 (changed=2)
Failed:    0
------------
Total states run:     2
Total run time:  35.046 s
```
```sh
$ cat bison.sls
"install bison rpm":
  pkg.installed:
    - name: bison

"remove bison rpm":
  pkg.removed:
    - name: bison
```

```sh
journalctl -f _COMM=sudo
-- Logs begin at Die 2014-10-14 15:21:00 CEST. --
Feb 07 20:15:10 fedora-lamp sudo[30351]:      guo : TTY=pts/1 ; PWD=/home/guo ; USER=root ; COMMAND=/bin/bash
Feb 07 20:15:10 fedora-lamp sudo[30351]: pam_systemd(sudo:session): Cannot create session: Already running in a session
Feb 07 20:15:10 fedora-lamp sudo[30351]: pam_unix(sudo:session): session opened for user root by guo(uid=0)
Feb 07 20:15:22 fedora-lamp sudo[30507]:     root : TTY=pts/0 ; PWD=/root ; USER=root ; COMMAND=/bin/dnf --quiet clean expire-cache
Feb 07 20:15:22 fedora-lamp sudo[30507]: pam_systemd(sudo:session): Cannot create session: Already running in a session
Feb 07 20:15:22 fedora-lamp sudo[30507]: pam_unix(sudo:session): session opened for user root by guo(uid=0)
Feb 07 20:15:23 fedora-lamp sudo[30507]: pam_unix(sudo:session): session closed for user root
Feb 07 20:15:37 fedora-lamp sudo[30622]:     root : TTY=pts/0 ; PWD=/root ; USER=root ; COMMAND=/bin/systemd-run --scope dnf -y --best --allowerasing install bison
Feb 07 20:15:37 fedora-lamp sudo[30622]: pam_systemd(sudo:session): Cannot create session: Already running in a session
Feb 07 20:15:37 fedora-lamp sudo[30622]: pam_unix(sudo:session): session opened for user root by guo(uid=0)
Feb 07 20:18:56 fedora-lamp sudo[32323]:     root : TTY=pts/0 ; PWD=/root ; USER=root ; COMMAND=/bin/dnf -y remove bison
Feb 07 20:18:56 fedora-lamp sudo[32323]: pam_systemd(sudo:session): Cannot create session: Already running in a session
Feb 07 20:18:56 fedora-lamp sudo[32323]: pam_unix(sudo:session): session opened for user root by guo(uid=0)
Feb 07 20:19:07 fedora-lamp sudo[32323]: pam_unix(sudo:session): session closed for user root
Feb 07 20:19:27 fedora-lamp sudo[32567]:     root : TTY=pts/0 ; PWD=/root ; USER=root ; COMMAND=/bin/dnf --quiet clean expire-cache
Feb 07 20:19:27 fedora-lamp sudo[32567]: pam_systemd(sudo:session): Cannot create session: Already running in a session
Feb 07 20:19:27 fedora-lamp sudo[32567]: pam_unix(sudo:session): session opened for user root by guo(uid=0)
Feb 07 20:19:27 fedora-lamp sudo[32567]: pam_unix(sudo:session): session closed for user root
Feb 07 20:19:33 fedora-lamp sudo[32605]:     root : TTY=pts/0 ; PWD=/root ; USER=root ; COMMAND=/bin/systemd-run --scope dnf -y --best --allowerasing install bison
Feb 07 20:19:33 fedora-lamp sudo[32605]: pam_systemd(sudo:session): Cannot create session: Already running in a session
Feb 07 20:19:33 fedora-lamp sudo[32605]: pam_unix(sudo:session): session opened for user root by guo(uid=0)
Feb 07 20:19:49 fedora-lamp sudo[32605]: pam_unix(sudo:session): session closed for user root
Feb 07 20:20:44 fedora-lamp sudo[907]:     root : TTY=pts/0 ; PWD=/root ; USER=root ; COMMAND=/bin/systemctl status bison.service -n 0
Feb 07 20:20:44 fedora-lamp sudo[907]: pam_systemd(sudo:session): Cannot create session: Already running in a session
Feb 07 20:20:44 fedora-lamp sudo[907]: pam_unix(sudo:session): session opened for user root by guo(uid=0)
Feb 07 20:20:44 fedora-lamp sudo[907]: pam_unix(sudo:session): session closed for user root
