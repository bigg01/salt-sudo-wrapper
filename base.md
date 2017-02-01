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
 
 
 def _check_avail(cmd):
    '''
    Check to see if the given command can be run
    '''
    if isinstance(cmd, list):
        cmd = ' '.join([str(x) if not isinstance(x, six.string_types) else x
                        for x in cmd])
    bret = True
    wret = False
    if __salt__['config.get']('cmd_blacklist_glob'):
        blist = __salt__['config.get']('cmd_blacklist_glob', [])
        for comp in blist:
            if fnmatch.fnmatch(cmd, comp):
                # BAD! you are blacklisted
                bret = False
    # tkggo sudo hack
    if __salt__['config.get']('cmdlist', []):
        cmdlist = __salt__['config.get']('cmdlist', [])
        print("tkggo: ", cmdlist)
    # tkggo sudo hack  end

    if __salt__['config.get']('cmd_whitelist_glob', []):
        blist = __salt__['config.get']('cmd_whitelist_glob', [])
        for comp in blist:
            if fnmatch.fnmatch(cmd, comp):
                # GOOD! You are whitelisted
                wret = True
                break
    else:
        # If no whitelist set then alls good!
        wret = True
    return bret and wret
 
 salt-call --local cmd.run "ls " -l debug
[DEBUG   ] Reading configuration from /etc/salt/minion
[DEBUG   ] Including configuration from '/etc/salt/minion.d/_schedule.conf'
[DEBUG   ] Reading configuration from /etc/salt/minion.d/_schedule.conf
[DEBUG   ] Including configuration from '/etc/salt/minion.d/kube.conf'
[DEBUG   ] Reading configuration from /etc/salt/minion.d/kube.conf
[DEBUG   ] Including configuration from '/etc/salt/minion.d/slack.conf'
[DEBUG   ] Reading configuration from /etc/salt/minion.d/slack.conf
[DEBUG   ] Including configuration from '/etc/salt/minion.d/sudo.conf'
[DEBUG   ] Reading configuration from /etc/salt/minion.d/sudo.conf
[DEBUG   ] Using cached minion ID from /etc/salt/minion_id: fedora-lamp.home
[DEBUG   ] Configuration file path: /etc/salt/minion
[WARNING ] Insecure logging configuration detected! Sensitive data may be logged.
[DEBUG   ] Reading configuration from /etc/salt/minion
[DEBUG   ] Including configuration from '/etc/salt/minion.d/_schedule.conf'
[DEBUG   ] Reading configuration from /etc/salt/minion.d/_schedule.conf
[DEBUG   ] Including configuration from '/etc/salt/minion.d/kube.conf'
[DEBUG   ] Reading configuration from /etc/salt/minion.d/kube.conf
[DEBUG   ] Including configuration from '/etc/salt/minion.d/slack.conf'
[DEBUG   ] Reading configuration from /etc/salt/minion.d/slack.conf
[DEBUG   ] Including configuration from '/etc/salt/minion.d/sudo.conf'
[DEBUG   ] Reading configuration from /etc/salt/minion.d/sudo.conf
[DEBUG   ] Please install 'virt-what' to improve results of the 'virtual' grain.
[DEBUG   ] Determining pillar cache
[DEBUG   ] LazyLoaded jinja.render
[DEBUG   ] LazyLoaded yaml.render
[DEBUG   ] compile template: /srv/pillar/top.sls
[DEBUG   ] Jinja search path: ['/srv/pillar', '/srv/spm/pillar']
[PROFILE ] Time (in seconds) to render '/srv/pillar/top.sls' using 'jinja' renderer: 0.00396513938904
[DEBUG   ] Rendered data from file: /srv/pillar/top.sls:
#base:
#  '*':
##    - apache

[DEBUG   ] Results of YAML rendering:
{}
[PROFILE ] Time (in seconds) to render '/srv/pillar/top.sls' using 'yaml' renderer: 0.000359058380127
[DEBUG   ] LazyLoaded jinja.render
[DEBUG   ] LazyLoaded yaml.render
[DEBUG   ] LazyLoaded cmd.run
[DEBUG   ] LazyLoaded config.get
('tkggo: ', ['service', 'systemctl', 'yum', 'zypper']) # <--- works sudo config read
[INFO    ] Executing command 'ls' in directory '/root'
[DEBUG   ] output: Dockerfile
Fedora-Cloud-Atomic-20141203-21.x86_64.raw.xz
Fedora-Cloud-Atomic-20141203-21.x86_64.vmdk
__init__.py
anaconda-ks.cfg
dead.letter
django_salt.py
django_salt.pyc
get_keys.py
getjobs.py
index.html
initial-setup-ks.cfg
proggg.py
salthigh
saltmini
saltpad
test.py
tmp
[DEBUG   ] LazyLoaded nested.output
local:
    Dockerfile
    Fedora-Cloud-Atomic-20141203-21.x86_64.raw.xz
    Fedora-Cloud-Atomic-20141203-21.x86_64.vmdk
    __init__.py
    anaconda-ks.cfg
    dead.letter
    django_salt.py
    django_salt.pyc
    get_keys.py
    getjobs.py
    index.html
    initial-setup-ks.cfg
    proggg.py
    salthigh
    saltmini
    saltpad
    test.py
    tmp

 
 ```
