# Barbara Liskov

## Description
> Barbara Liskov (born November 7, 1939 as Barbara Jane Huberman) is an American computer scientist who has made pioneering contributions to programming languages and distributed computing. Her notable work includes the development of the Liskov substitution principle which describes the fundamental nature of data abstraction, and is used in type theory (see subtyping) and in object-oriented programming (see inheritance). Her work was recognized with the 2008 Turing Award, the highest distinction in computer science. - Wikipedia Entry

> Chal: Return the flag back to the 2008 Turing Award Winner.

### Attachments
[BarbaraLiskov.pyc](./BarbaraLiskov.pyc)

## Solution
* Decompyle3 and uncompyle6 dont work on this file.
* Open pyc in a text editor and find the a base64 encoded string.
* Find string `Y2hjdGZ7dV9uM3Yzcl9uMzNkXzBwdDFtNGxfcDNyZjBybTRuYzMsX3VfbjMzZF9nMDBkLTNuMHVnaF9wM3JmMHJtNG5jM30=`
* Base64 decode it
```zsh 
$ echo -n "Y2hjdGZ7dV9uM3Yzcl9uMzNkXzBwdDFtNGxfcDNyZjBybTRuYzMsX3VfbjMzZF9nMDBkLTNuMHVnaF9wM3JmMHJtNG5jM30=" | base64 -d
chctf{u_n3v3r_n33d_0pt1m4l_p3rf0rm4nc3,_u_n33d_g00d-3n0ugh_p3rf0rm4nc3}
```

## Alternate Solution
* Run `strings` on the file and get the base64 encoded string
* Base64 decode it.

### FLAG
```
chctf{u_n3v3r_n33d_0pt1m4l_p3rf0rm4nc3,_u_n33d_g00d-3n0ugh_p3rf0rm4nc3}
```