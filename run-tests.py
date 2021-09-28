from email.policy import default
import subprocess as cmd
import os
import optparse
from time import sleep

parser = optparse.OptionParser()

parser.add_option('-d' , '--dir' , dest='dir' , help='Path of the directory in which the files are to test' , default=None)

options , args = parser.parse_args()

# print(options.dir)

if not options.dir or str(options.dir)=='.':
    cwd = os.getcwd()
else:
    cwd = str(options.dir)

cmd.run('python -m pip install pyflakes' , shell=True , cwd=cwd)
cmd.run('python -m pip install pylint' , shell=True , cwd=cwd)

files_n_dirs = os.listdir()

files_to_test = list()

for file in files_n_dirs:
    if file.endswith('.py'):
        files_to_test.append(file)

print('The following files will be checked:\n')

for file in files_to_test:
    print(f'  ./{file}')

sleep(3)

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

print('Checking Done!')
