# Time Traveler's Git (Part 1)

## Description
> You are a time traveler who stumbled upon an ancient Git repository containing valuable data from a long-gone era. However, the repository seems to have some hidden secrets and potential vulnerabilities in its history. Charlie is your friend.

`143.110.189.89`

## Solution
* We are given an IP address.
* Running a quick **nmap** scan on the IP address, we find that port 22 is open.
* We can login to the ftp server using `anonymous` as the username. 
```bash
ftp 143.110.180.89
Connected to 143.110.180.89.
220 (vsFTPd 3.0.5)
Name (143.110.180.89:ssk): anonymous
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls -al
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
dr-xr-xr-x  1    1000   1000    4096 Jul 25 10:31 .
dr-xr-xr-x  1    1000   1000    4096 Jul 25 10:31 ..
drwxrwxr-x  8    0      0       4096 Apr 09 18:58 .git
-rw-rw-r--  1    0      0       514  Apr 09 18:58 login.html
226 Directory send OK.
```
* Download everything from **.git** and **login.html** using ftp
    * I downloaded everything manually like a noob.
    * Alternative way:   
    `wget -r --no-passive --no-parent --user=anonymous --password=anonymous ftp://143.110.180.89`
* Check the logs  
`git log`

```
commit 00231aa51594c4d44631ce9237255fe779afa72c (HEAD -> main, origin/main, origin/HEAD)
Author: 4dity4k <k2000aditya@yahoo.com>
Date:   Mon Apr 10 00:25:47 2023 +0530

    Smart cookie

commit b5488e6d7b3e27949d825292fa992562333c1de9
Author: 4dity4k <k2000aditya@yahoo.com>
Date:   Sun Apr 9 23:43:58 2023 +0530

    Latest and fresh

commit 5a496dbebbce1585698634e5348703b74e7ac781
Author: 4dity4k <k2000aditya@yahoo.com>
Date:   Sun Apr 9 23:20:43 2023 +0530

    My first web application
```

* Check the first commit:
`git checkout 5a496dbebbce1585698634e5348703b74e7ac781`
* We find an **SSH** key
* Copy it to a file and change the permissions:  (**MAKE SURE THE FORMAT IS RIGHT!!!**)  
`chmod 600 id_rsa`
* Login to the server using the ssh key:  
`ssh -i id_rsa charlie@0.cloud.chals.io -p <port-no>` 
* List the files:
```sh
$ ls
user.txt
$ cat user.txt
KPMG_CTF{324b7e52953f62f1624fb64a2e8202e4}
```
* FLAG:  
`KPMG_CTF{ed0d1d2926547a24488d29fb5c3941be}`
