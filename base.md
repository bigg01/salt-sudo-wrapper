```
Since all modules use "cmd" module for command execution you only need to modify that one module to get going with sudo.

Open cmdmod.py and look for this part of code:

try:
    proc = salt.utils.timed_subprocess.TimedProc(cmd, **kwargs)
except (OSError, IOError) as exc:
    raise CommandExecutionError('Unable to run command: {0}'.format(exc))

You could simply prepend "sudo " to cmd parameter but you don't really want to wrap everything with sudo. You need some way to define what to wrap and what to leave as is.

I've solved this by adding a parameter to my minion configuration:

cmd.wrapper: /var/lib/salt/wrapper/maybesudo

Initialize our new parameter at the beginning in cmdmod.py:

__opts__ = {
            'cmd.wrapper': ""
           }

And before command gets executed add this:

if __opts__['cmd.wrapper']:
    if isinstance(cmd, str):
        cmd = __opts__['cmd.wrapper'] + ' ' + cmd
    else:
        cmd.insert(0, __opts__['cmd.wrapper'])

So instead of wrapping everything with sudo we've wrapped everything with a simple bash script that check whether it needs to run command as sudo or not.

My maybesudo script:

#!/bin/sh
if /bin/grep -q -x "$1" /var/lib/salt/wrapper/commands
then
    exec /usr/bin/sudo "$@"
else
    exec "$@"
fi
```

```
sudo salt-call --local  config.get cmdlist
local:
    - service
    - systemctl
    - yum
    - zypper
sudo cat  /etc/salt/minion.d/sudo.conf
cmdlist:
 - service
 - systemctl
 - yum
 - zypper
 ```
