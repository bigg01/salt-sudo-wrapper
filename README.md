# salt-sudo-wrapper


```
vi cmdmod.py

def _run(cmd,
         cwd=None,
         stdin=None,
         stdout=subprocess.PIPE,
         stderr=subprocess.PIPE,
         output_loglevel='debug',
         log_callback=None,
         runas=None,
         shell=DEFAULT_SHELL,
         python_shell=False,
         env=None,
         clean_env=False,
         rstrip=True,
         template=None,
         umask=None,
         timeout=None,
         with_communicate=True,
         reset_system_locale=True,
         ignore_retcode=False,
         saltenv='base',
         pillarenv=None,
         pillar_override=None,
         use_vt=False,
         password=None,
         bg=False,
         encoded_cmd=False,
         **kwargs):
    '''
    Do the DRY thing and only call subprocess.Popen() once
    '''
    if 'pillar' in kwargs and not pillar_override:
        pillar_override = kwargs['pillar']
    if _is_valid_shell(shell) is False:
        log.warning(
            'Attempt to run a shell command with what may be an invalid shell! '
            'Check to ensure that the shell <{0}> is valid for this user.'
            .format(shell))

    log_callback = _check_cb(log_callback)

    # tkggo
    if 'sudo' in kwargs:
        log.debug('tkggo hack sudo')
        sudocmd = which('sudo')
        log.debug(sudocmd)
        if isinstance(cmd, str):
            cmd = sudocmd + ' ' + cmd
        else:
            cmd.insert(0, sudocmd)
      ```
            
 ```           
     # run tvest
            salt-call --local cmd.run "yum info bash" sudo=True -l info
[INFO    ] Executing command '/bin/sudo yum info bash' in directory '/root'
local:
    Redirecting to '/usr/bin/dnf info bash' (see 'man yum2dnf')

    Last metadata expiration check: 0:52:37 ago on Wed Feb  1 10:05:44 2017.
    Installed Packages
    Name        : bash
    Arch        : x86_64
    Epoch       : 0
    Version     : 4.3.42
    Release     : 7.fc24
    Size        : 6.1 M
    Repo        : @System
    From repo   : updates
    Summary     : The GNU Bourne Again shell
    URL         : http://www.gnu.org/software/bash
    License     : GPLv3+
    Description : The GNU Bourne Again shell (Bash) is a shell or command language
                : interpreter that is compatible with the Bourne shell (sh). Bash
                : incorporates useful features from the Korn shell (ksh) and the C
                : shell (csh). Most sh scripts can be run by bash without
                
                
   # no sudo kwargs
   
   salt-call --local cmd.run "yum info bash"  -l info
[INFO    ] Executing command 'yum info bash' in directory '/root'
local:
    Redirecting to '/usr/bin/dnf info bash' (see 'man yum2dnf')

    Last metadata expiration check: 0:53:14 ago on Wed Feb  1 10:05:44 2017.
    Installed Packages
    Name        : bash
    Arch        : x86_64
    Epoch       : 0
    Version     : 4.3.42
    Release     : 7.fc24
    Size        : 6.1 M
    Repo        : @System
    From repo   : updates
    Summary     : The GNU Bourne Again shell
    URL         : http://www.gnu.org/software/bash
    License     : GPLv3+
    Description : The GNU Bourne Again shell (Bash) is a shell or command language
                : interpreter that is compatible with the Bourne shell (sh). Bash
                : incorporates useful features from the Korn shell (ksh) and the C
                : shell (csh). Most sh scripts can be run by bash without
            ```
