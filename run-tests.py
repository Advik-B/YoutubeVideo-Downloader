import subprocess as cmd
import os
from time import sleep

cwd  = os.getcwd()

cmd.run('python -m pip install pyflakes' , timeout=10)
cmd.run('python -m pip install pylint' , timeout=10)

ignore_paths = [

    '__init__.py',

    'run-tests.py'
]

files_n_dirs = os.listdir()

pyflakes_version = cmd.check_output('py -m pyflakes -V')

files_to_test = list()


for file in files_n_dirs:
    if file.endswith('.py'):
        files_to_test.append(file)

print('The following files will be checked:\n')

for file in files_to_test:
    print(f'  ./{file}')

print()
print('-'*80)
print('*'*80)
print('-'*80)
print()


for file in files_to_test:
    print(f'Checking: ./{file} 🔎')
    print()
    o = cmd.getoutput(f'py -m pyflakes ./{file}')
    p = cmd.getoutput(f'py -m pylint ./{file}')

    if not o or not p:
        print('No problems found!')
    else:
        print('pyflakes:\n' , o)
        print()
        print()
        print('*'*80)
        print()
        print()
        print('pylint:\n\t' , p)

    if p:
        print('Suggestions:\n')
        print(p.replace('************* ' , ''))
    # print(p)
    sleep(3)
    print()
    print('-'*80)
    print()

print('aa')