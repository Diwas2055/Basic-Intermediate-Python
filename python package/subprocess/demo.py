# A subprocess in Python is a task that a python script delegates to the Operative system (OS).
# The subprocess library allows us to execute and manage subprocesses directly from Python. 
# That involves working with the standard input (stdin), standard output (stdout), and return codes.

# Standard input – This is the file-handle that a user program reads to get information from the user. We give input to the standard input (stdin).

# Standard output – The user program writes normal information to this file-handle. The output is returned via the Standard output (stdout).


# Example :- Set up a virtualenv with subprocess

import subprocess

from pathlib import Path


VENV_NAME = '.venv'
REQUIREMENTS = 'requirements.txt'

process1 = subprocess.run(['which', 'python3'], capture_output=True, text=True)

if process1.returncode != 0:
    raise OSError('Sorry python3 is not installed')

python_bin = process1.stdout.strip()

print(f'Python found in: {python_bin}')

process2 = subprocess.run('echo "$SHELL"', shell=True, capture_output=True, text=True)

shell_bin = process2.stdout.split('/')[-1]
print(f'Shell found in: {shell_bin}')

create_venv = subprocess.run([python_bin, '-m', 'venv', VENV_NAME], check=True)

if create_venv.returncode == 0:
    print(f'Your venv {VENV_NAME} has been created')

pip_bin = f'{VENV_NAME}/bin/pip3'

if Path(REQUIREMENTS).exists():
    print(f'Requirements file "{REQUIREMENTS}" found')
    print('Installing requirements')
    subprocess.run([pip_bin, 'install', '-r', REQUIREMENTS])

    print('Process completed! Now activate your environment with "source .venv/bin/activate"')

else:
    print("No requirements specified ...")