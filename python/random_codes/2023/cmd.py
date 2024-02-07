import subprocess

# Execute a Windows command
# subprocess.call('dir', shell=True)  # 'dir' is the Windows command to list directory contents

# Execute a Unix command
subprocess.call('espeak bengy', shell=True)  # 'ls' is the Unix command to list directory contents
