# Time Traveler_s Git (Part 2)

## Description
> You are a time traveler who stumbled upon an ancient Git repository containing valuable data from a long-gone era. However, the repository seems to have some hidden secrets and potential vulnerabilities in its history.

`143.110.180.89`

## Solution
* This is the next part of Time Traveler's Git (Part 1)
* Using the same `id_rsa` file we got from part 1, we can ssh into the server.
* Check for binaries with the SUID bit set:  
`find / -perm -u=s -type f 2>/dev/null`
* We find `/zsh` which is a binary that is not normally set with the SUID bit.
* Running the command:  
`/usr/bin/zsh`  
Gives us a root shell. You can confirm this by running `whoami`
* Now, we can read the flag in the root directory.
`cat /root/root.txt`
* Flag:  
`KPMG_CTF{27d67906ecd422971944f23c8afd3bd8}`
