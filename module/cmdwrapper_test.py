from functools import wraps

import os
import signal
import subprocess

import shutil


def which(file):
    for path in os.environ["PATH"].split(os.pathsep):
        if os.path.exists(os.path.join(path, file)):
                return os.path.join(path, file)
    return None

def sudocmd():
    return str(which('sudo'))

def sudo(cmd):
    sudocmd = '/usr/bin/sudo' #sudocmd()
    def sudo_decorator(func):
        @wraps(func)
        def func_wrapper(cmd):
            if isinstance(cmd, str):
                cmd = sudocmd + ' ' + cmd
            if isinstance(cmd, list):
                cmd.insert(0, sudocmd)
            return "sudo {0}".format(cmd)
        return func_wrapper
    return sudo_decorator


@sudo("cmd")
def _run(cmd):
    """returns some text"""
    return cmd

def _run2(cmd):
    """returns some text"""
    return cmd
    
print(_run('ls'))

print(_run(['ls', '-la']))

print(_run2('ls'))

print(_run2(['ls', '-la']))
