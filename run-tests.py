import subprocess as cmd
import os
from time import sleep

cwd  = os.getcwd()

cmd.run('python -m pip install pyflakes' , shell=True)
cmd.run('python -m pip install pylint' , shell=True)

ignore_paths = [

    '__init__.py',

    'run-tests.py'
]

files_n_dirs = os.listdir()

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
    o = cmd.getoutput(f'python -m pyflakes ./{file}')
    p = cmd.getoutput(f'python -m pylint ./{file}')

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
    # print(p)
    sleep(3)
    print()
    print('-'*80)
    print()

print('aa')