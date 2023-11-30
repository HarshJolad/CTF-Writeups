# Hot and Cold

## Description
> Find the flag hidden in this labyrinth.

[files.tar.gz](./files.tar.gz)

## Solution
* Unzip using `gunzip`
```
$ gunzip files.tar.gz
```
* Unzip using `tar`
```
$ tar -xf files.tar
```
* The extracted folder contains a many folders inside it.
* View all the folder contents using 
```
tree -a
```
* We see a `flag.txt` but its hidden
* Opening it gives us the flag

### FLAG
```
pesu_ec{wh04_7h47_w45_50_h07}
```