# six wrapper module
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
