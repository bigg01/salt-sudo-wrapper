from functools import wraps

import os
import signal
import subprocess

import shutil

sudocmd = None


def which(file):
    for path in os.environ["PATH"].split(os.pathsep):
        if os.path.exists(os.path.join(path, file)):
                return os.path.join(path, file)
    return None

def sudocmd():
    return str(which('sudo'))

def sudo(cmd):
    sudocmd = sudocmd()
    def tags_decorator(func):
        @wraps(func)
        def func_wrapper(cmd):
            if isinstance(cmd, str):
                cmd = sudocmd + ' ' + cmd
            if isinstance(cmd, list):
                cmd.insert(0, sudocmd)
            return "sudo {0}".format(cmd)
        return func_wrapper
    return tags_decorator


@sudo("cmd")
def _run(cmd):
    """returns some text"""
    return 'systemctl restart test1'

print(_run('ls'))

print(_run(['ls', '-la']))

print(sudocmd())
