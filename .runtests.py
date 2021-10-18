import os
from fnmatch import fnmatch
from subprocess import run
from termcolor import cprint
import _pytest

def listfiles(root, pattern:str='*.*'):
    A = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            if fnmatch(name, pattern):
                A.append(os.path.join(path, name))
    return A

files_to_test = listfiles(os.getcwd(), '*.py')
fnames = []

for filename in files_to_test:
    fnames.append("%s\tin '%s'" % (filename.split('\\')[-1], filename))
cprint('Running tests for the following file(s):', color='green' ,attrs=['bold', 'underline'])
print()
for file in fnames:
    cprint(':: '+file, color='yellow')

print()

for file in files_to_test:
    if file.split('\\')[-1] == '.runtests.py':
        pass
    else:
        cprint('Testing: %s' % file#.
            , 'green', attrs=['bold'])
        print()
        cprint((f'{":"*40}: START :{":"*40}').center(80) ,'cyan', attrs=['reverse', 'bold'])
        run('python3 -m pytest %s' % file, timeout=20, shell=True)
        cprint((f'{":"*40}: END :{":"*40}').center(80) ,'cyan', attrs=['reverse', 'bold'])
        print('\n'*4)

cprint('ALL TESTS COMPLETED', color='green', attrs=['bold', 'reverse', 'underline'])
exit(0)